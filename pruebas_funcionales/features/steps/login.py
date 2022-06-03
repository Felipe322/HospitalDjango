from behave import given, when, then
import time

@given(u'que ingreso el usuario "{usuario}"')
def step_impl(context, usuario):
    context.driver.get(context.url + '/login')
    context.driver.find_element_by_name('username').send_keys(usuario)


@given(u'la contraseña "{password}"')
def step_impl(context, password):
    context.driver.find_element_by_name('password').send_keys(password)



@when(u'presiono el botón Ingresar')
def step_impl(context):
    context.driver.find_element_by_tag_name('button').click()
    time.sleep(0.5)


@then(u'puedo ver en la página principal el nombre de mi usuario "{usuario}"')
def step_impl(context, usuario):
    respuesta = context.driver.find_element_by_partial_link_text(usuario).text
    assert usuario in respuesta
