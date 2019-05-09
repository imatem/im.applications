# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s im.applications -t test_coloquio_application.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src im.applications.testing.IM_APPLICATIONS_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/im/applications/tests/robot/test_coloquio_application.robot
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

Scenario: As a site administrator I can add a coloquio_application
  Given a logged-in site administrator
    and an add coloquio_application form
   When I type 'My coloquio_application' into the title field
    and I submit the form
   Then a coloquio_application with the title 'My coloquio_application' has been created

Scenario: As a site administrator I can view a coloquio_application
  Given a logged-in site administrator
    and a coloquio_application 'My coloquio_application'
   When I go to the coloquio_application view
   Then I can see the coloquio_application title 'My coloquio_application'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add coloquio_application form
  Go To  ${PLONE_URL}/++add++coloquio_application

a coloquio_application 'My coloquio_application'
  Create content  type=coloquio_application  id=my-coloquio_application  title=My coloquio_application

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the coloquio_application view
  Go To  ${PLONE_URL}/my-coloquio_application
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a coloquio_application with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the coloquio_application title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
