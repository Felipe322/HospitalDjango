from behave import given, when, then
import time

@given(u'que estoy dentro del sistema')
def step_impl(context):
    login(context)


@given(u'entro a la sección de registro de pacientes')
def step_impl(context):
    context.driver.find_element_by_xpath('/html/body/div[1]/aside[1]/div/div[4]/div/div/nav/ul/li[2]/a').click()
    time.sleep(0.5)
    context.driver.find_element_by_xpath('/html/body/div[1]/aside[1]/div/div[4]/div/div/nav/ul/li[2]/ul/li[2]/a').click()


@given(u'capturo los datos: nombre "{nombre}", apellido paterno: "{primer}", apellido materno "{segundo}"')
def step_impl(context, nombre, primer, segundo):
    context.driver.find_element_by_name('nombre').send_keys(nombre)
    context.driver.find_element_by_name('primerApellido').send_keys(primer)
    context.driver.find_element_by_name('segundoApellido').send_keys(segundo)


@given(u'el número de seguro social "{numero_ss}", fecha de nacimiento "{fecha_nac}", tipo de sangre "{tipo_sangre}"')
def step_impl(context, numero_ss, fecha_nac, tipo_sangre):
    context.driver.find_element_by_name('numero_ss').send_keys(numero_ss)
    context.driver.find_element_by_name('fecha_nac').send_keys(fecha_nac)
    context.driver.find_element_by_name('tipo_sangre').send_keys(tipo_sangre)
    


@given(u'el estado "{estado}" del municipio "{municipio}"')
def step_impl(context, estado, municipio):
    context.driver.find_element_by_name('estado').send_keys(estado)
    context.driver.find_element_by_name('municipio').send_keys(municipio)


@when(u'presiono el botón Agregar')
def step_impl(context):
    context.driver.find_element_by_tag_name('html').send_keys(context.keys.END)
    time.sleep(0.5)
    context.driver.find_element_by_xpath('/html/body/div[1]/div[1]/section/div/div[1]/div[2]/div/form/div[2]/input').click()
    time.sleep(0.5)


@then(u'puedo ver el paciente "{paciente}" en la lista de pacientes registrados.')
def step_impl(context, paciente):
    tbody = context.driver.find_element_by_tag_name('tbody')
    trs = tbody.find_elements_by_tag_name('tr')
    lista_pacientes = []
    for tr in trs:
        tds = tr.find_elements_by_tag_name('td')
        nombre = tds[0].text + " " + tds[1].text + " " + tds[2].text
        lista_pacientes.append(nombre)

    print (str(lista_pacientes))
    context.test.assertIn(paciente, lista_pacientes)




def login(context):
    context.driver.get(context.url + '/login')
    context.driver.find_element_by_name('username').send_keys("alex@asdas.mx")
    context.driver.find_element_by_name('password').send_keys("alex123")
    context.driver.find_element_by_tag_name('button').click()
    time.sleep(0.5)
