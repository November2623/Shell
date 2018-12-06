1. The name of the team: dnhu - hxvien - kmduy


2. The working hours/days each member commits to: at least 35 hours per week (about 5 hours a day)
      + We meet up at less three times a week, for discussing about all of the problem and merge code
      + The fixed time: 2.00pm on Mon, Wed, Fri every week
      + The timetable of each member at INTEK:
            + dnhu: 11:00am - 7:00pm from Mon to Sat, full time Wednesday
            + hxvien: afternoon Monday, Wednesday, Friday, full time at Thursday and Sunday
            + kmduy : *duy, please fill in here*


3. How often you will check-in with each others' progress: 2 days/ times


4. The strengths and weaknesses of each member, and how to leverage/mitigate them for the project:
      + dnhu:
              - strengths: the ability to use the search engine efficiently, fast-learner
              - weaknesses: lack of time, having difficulties using English
      + hxvien:
              - strengths: creative
              - weaknesses: unclear code, lack of time

      + kmduy:
              - strengths: *duy, please fill in here*
              - weaknesses: *duy, please fill in here*

5. The allocation of the workload: *The status: research => implement => test => done*
      + Date: Wed 28/11/2018 - 1st => *MEMBERS* : DNHU, HXVIEN, KMDUY JOINED THE MEETING
              _CONTENT_ : DIVISION FOR THE PROJECT
              _DISCUSSTION_ :
                    + Each person choose 3 features to research.  
                    + All team members make sure ready for implementing after researching or switching if it needed
              _REPORT_ :
                    + dnhu:
                            + globbing: research
                            + word expansions: research
                            + pipes & the redirections: research

                    + hxvien:
                            + signals handling: research
                            + subshells with: research
                            + quoting (quotes & escape characters): research

                    + kmduy:
                            + handling the exit status of commands: research
                            + command substitution with the back quotes: research
                            + logical operators && and ||: research
                _NOTE FOR THE NEXT TIME_:
                      NULL

      + Date: Fri 30/11/2018 - 2rd => *MEMBERS* : ONLY HXVIEN AT INTEK THIS TIME
                _REPORT_ :
                    + dnhu:
                            + globbing:
                                      + research: done the basic document
                                      + implementing: go on
                            + word expansions:  
                                      + research: done the basic document
                                      + implementing: go on
                            + pipes & the redirections:
                                      + research : adding note for basic document for research, researching more
                                      + implement : not yet
                    + hxvien:
                            + signals handling:
                                      + research:
                                      + implementing: go on
                            + subshells with:
                                      + research:  - Not sure the main idea of the feature.
                                                   - Can be switch or research more, it's up to hxvien
                            + quoting (quotes & escape characters):
                                      + research:
                                      + implementing: go on
                    + kmduy:
                            + handling the exit status of commands: NONE feedback
                            + command substitution with the back quotes: NONE feedback
                            + logical operators && and ||: NONE feedback
                  _NOTE FOR THE NEXT TIME_:
                        1. Vien and Duy, please pay attention with somewhere I noted you need to fill in
                        2. Duy, please send team the feed back of your workload
                        3. I create a document directory for team in branch master,
                           all you guys need to write some basic note about the main idea of your part.
                           This helps other members follow you and your features.
                        4. All members will report to each other your process in the next time
                        5. *Focus on rebuilding the main structure*

      + Date: Mon 03/11/2018 - 3rd => *MEMBERS* : HXVIEN AND DNHU AT INTEK THIS TIME
                _CONTENT_ : FINISH THE MAIN STRUCTURE OF SHELL
                            Changing strategies and the way to approach this project
                            RE-DEAL THE TASK OF PROJECT
                _DISCUSSTION_ :
                      + DNHU and HXVIEN built the main structure and divided the module.
                      + All team members follow the workload of team and the point idea of the solution
                      + Deploy the main step to put the feature to the main structure:
                              + Make clear the using of each special characters => Implement each special characters independently  
                              + The priority and how to mix those with each other => more clearly in next time meet up
                _REPORT_ :
                      + dnhu: special character => ~, %, #, !, @, +, ( | ), ${PARAMETER}, $PARAMETER
                              + globbing:
                                        + research: continue searching deeply
                                        + implement: support and switch to HXVIEN, building Exclamatory Sign ! , @ , dot .  , + , logic OR ( | )
                              + path expansions:
                                        + tilde expansion: building ~
                                        + parameter expansion: building ${PARAMETER}, $PARAMETER
                              + DEEPLY RESEARCH and Responsible for writing the document: *IMPORTANT*
                                        1. IDENTIY THE FUNCTION/ THE BEHAVIOR OF THE SPECIAL CHARACTER
                                        2. handling the exit status of commands
                                        3. signals handling
                                        4. logical operators && and ||
                              <!-- + pipes & the redirections: nothing much => get last -->

                      + hxvien: special character => * , ? , [] , () , ' ' , " ", ^, (/)
                              + globbing:
                                        + implement (basic-globbing): building start * , question mark ? , Square Bracket []
                              + subshells with ():
                                        + research: team member supported him the main idea.
                                        + implement: building parentheses ()
                              + quoting (quotes & escape characters):
                                        + implement: building single quotes ' ', double quotes " ", escape characters ^, (maybe slack /)
                              <!-- + signals handling: nothing much => get last -->

                      + kmduy: special characte => ` `, $(), { }
                              + handle exit of shell => break out the prompt loop
                                        + implement: continue building and merge with the main structure later
                              + handling the exit status of commands:
                                        + implement: continue building, return the error number or run success
                              + command substitution with the back quotes(` `):
                                        + implement: back quotes `command` and $(command) is the same
                              <!-- + logical operators && and ||: nothing much => get last -->

                  _NOTE FOR THE NEXT TIME_:
                        1. All members make sure the main BEHAVIOR/STRUCTE of shell. (*Has been communicated to KMDUY in the evening*)
                        2. USING main structure to run the test case of the features.
                           If it crashes, please make sure the reason is your feature or structure?
                        3. Spend time to write basic document and a file contains the testcase of your task
                        4. Priority of building:
                              + DNHU: path expansion => deeply research => support globbing(Expand)
                              + HXVIEN: globbing(basic) => quoting => subshells
                              + KMDUY: exit of shell => exit status of commands => command substitution => support globbing(Expand)

      + Date: Wed 05/12/2018 - 4th
      + Date: Fri 07/11/2018 - 5th
      .....


6. The features you want to implement and how they interface together
