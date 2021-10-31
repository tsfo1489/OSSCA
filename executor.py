import contribution_evaluator as cv

if __name__ == "__main__":
    contributorDict = {}
    while(1):
        print("1: READ")
        print("2: ANALYSIS")
        print("q: quit")
        mode = input(">>>")
        
        if mode=='1' :
            while(1):
                print("1: Fetch all table and save json file")
                print("2: Fetch input table and save json file")
                print("3: Make yearly data")
                print("q: quit")
                num = input(">>>")
                if(num=='1'):
                    try :
                        tableNameList = ["github_overview","github_repo_commits","github_repo_contributor","github_repo_stats", "github_repo_stats_yymm","github_stats_yymm","student_tab"]
                        for tableName in tableNameList :
                            cv.saveJson(tableName)
                    except Exception as e:
                        print("error1: ",e)
                elif(num=='2'):
                    try :
                        print("Input table name:")
                        tableName = input(">>>")
                        cv.saveJson(tableName)
                    except Exception as e:
                        print("error2: ",e)
                elif(num=='3'):
                    try :
                        cv.savePeriodData()
                    except Exception as e:
                        print("error2: ",e)
                elif(num=='q'):
                    break
        elif mode == '2' :
            while(1) :
                print("a: all process")
                print("1: Json make contributor object")
                print("2: Contributor link repository data")
                print("3: anlyze commits data")
                print("4: Merge Json data and save json file")
                print("5: evaluate opensource score")

                print("9: Show contributor data")
                print("q: quit")
                num = input(">>>")
                if(num=='a'):
                    try:
                        contributorDict = cv.makeContributor()
                        contributorDict = cv.linkRepo(contributorDict)
                        cv.analyzeCommits(contributorDict)
                        cv.saveTotalJson(contributorDict)
                        cv.yieldScore(contributorDict)
                        print("done!")
                    except Exception as e:
                        print("error a: ",e)
                if(num=='1'):
                    try:
                        contributorDict = cv.makeContributor()
                    except Exception as e:
                        print("error1: ",e)
                elif(num=='2'):
                    try:
                        contributorDict = cv.linkRepo(contributorDict)
                    except Exception as e:
                        print("error2: ",e)
                elif(num=='3'):
                    try:
                        cv.analyzeCommits(contributorDict)
                    except Exception as e:
                        print("error3: ",e)
                elif(num=='4'):
                    try:
                        cv.saveTotalJson(contributorDict)
                    except Exception as e:
                        print("error4: ",e)
                elif(num=='5'):
                    try:
                        cv.yieldScore(contributorDict)
                    except Exception as e:
                        print("error5: ",e)
                elif(num=='9'):
                    try:
                        print("input contributor name")
                        name = input(">>>")
                        print("How should it print out? 1. Compact 2. Normal 3. Detail")
                        how = input(">>>")
                        contributorDict[name].showContribution(how)
                    except Exception as e:
                        print("error9: ",e)
                elif(num=='q'):
                    break
                else:
                    continue
        elif mode == 'q' :
            print("Bye!")
            break;