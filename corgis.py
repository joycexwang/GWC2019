
import cancer
from textblob import TextBlob
list_of_report = cancer.get_reports(test=False)
# print(list_of_report)

cancer_rate_list = []
state_list = []

for person in list_of_report:
    human = person["Data"]["Count"]
    cancer_rate_list.append(human)
print(cancer_rate_list)
    #for year in list_of_report:
        #if number > latest:
            #latest = number
            #latest_list.append(latest)
#print(latest_list)

for state in list_of_report:
    area = state["Area"]
    if area not in state_list:
        state_list.append(area)
print(state_list)
