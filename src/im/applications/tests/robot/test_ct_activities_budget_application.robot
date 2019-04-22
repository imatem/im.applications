# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s im.applications -t test_activities_budget_application.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src im.applications.testing.IM_APPLICATIONS_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/im/applications/tests/robot/test_activities_budget_application.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Activities Budget Application
  Given a logged-in site administrator
    and an add Activities Budget Application form
   When I type 'My Activities Budget Application' into the title field
    and I submit the form
   Then a Activities Budget Application with the title 'My Activities Budget Application' has been created

Scenario: As a site administrator I can view a Activities Budget Application
  Given a logged-in site administrator
    and a Activities Budget Application 'My Activities Budget Application'
   When I go to the Activities Budget Application view
   Then I can see the Activities Budget Application title 'My Activities Budget Application'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Activities Budget Application form
  Go To  ${PLONE_URL}/++add++Activities Budget Application

a Activities Budget Application 'My Activities Budget Application'
  Create content  type=Activities Budget Application  id=my-activities_budget_application  title=My Activities Budget Application

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Activities Budget Application view
  Go To  ${PLONE_URL}/my-activities_budget_application
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Activities Budget Application with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Activities Budget Application title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
