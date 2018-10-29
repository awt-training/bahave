from behave import given


@given(u'This is testing background for "AWT-01"')
def step_impl(context):
    print(u'STEP: Given This is testing background for "AWT-01"')
