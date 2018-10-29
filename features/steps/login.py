from behave import given, when, then


@given(u"the ninja has a third level black-belt")
def step_the_ninja_has_a_third_level_black_belt(context):
    print("This is the first step")



@when(u'attacked by a samurai')
def step_impl(context):
    print("This is the second step")


@then(u'the ninja should engage the opponent')
def step_impl(context):
    print("This is the third step")


@given(u'I put {thing} in a blender,')
def step_impl(context, thing):
    print "Scenario Outline"
    print context
    print thing


@when(u'I switch the blender on')
def step_impl(context):
    print(u'STEP: When I switch the blender on')


@then(u'it should transform into {other_thing}')
def step_impl(context, other_thing):
    print "Scenario Outline"
    print context
    print "Other thing is {}".format(other_thing)


@given(u'a set of specific users')
def step_impl(context):
    print "TABLE input"
    for row in context.table:
        print("name={} department={}".format(row['name'], row['department']))


@when(u'we count the number of people in each department')
def step_impl(context):
    print(u'STEP: When we count the number of people in each department')


@then(u'we will find two people in "{text}"')
def step_impl(context, text):
    print(u'STEP: Then we will find two people in "{}"'.format(text))


@then(u'we will find one person in "{text}"')
def step_implementation(context, text):
    print(u'STEP: Then we will find one person in "{}"'.format(text))
    print("**************************************")
    step_impl13(context)


@when(u'I do the same thing as before')
def step_impl13(context):
    print(u"STEPS INSIDE OTHER STEP")
    context.execute_steps(u'''
     Given a set of specific users
      | name      | department  |
      | Barry     | Beer Cans   |
      | Pudey     | Silly Walks |
     When I switch the blender on
    ''')
