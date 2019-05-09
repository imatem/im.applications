# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s im.applications -t test_moneysack.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src im.applications.testing.IM_APPLICATIONS_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/im/applications/tests/robot/test_moneysack.robot
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

Scenario: As a site administrator I can add a moneysack
  Given a logged-in site administrator
    and an add moneysack form
   When I type 'My moneysack' into the title field
    and I submit the form
   Then a moneysack with the title 'My moneysack' has been created

Scenario: As a site administrator I can view a moneysack
  Given a logged-in site administrator
    and a moneysack 'My moneysack'
   When I go to the moneysack view
   Then I can see the moneysack title 'My moneysack'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add moneysack form
  Go To  ${PLONE_URL}/++add++moneysack

a moneysack 'My moneysack'
  Create content  type=moneysack  id=my-moneysack  title=My moneysack

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the moneysack view
  Go To  ${PLONE_URL}/my-moneysack
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a moneysack with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the moneysack title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
