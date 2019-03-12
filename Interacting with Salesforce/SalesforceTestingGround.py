from simple_salesforce import Salesforce

# sf = Salesforce(username='sreitz@globaltiesus.org', password='5TeveSharesHisPasswordWithBridge!', security_token='wir42kooHJ3ZVHnu7J33NbAg', domain='test')

sf = Salesforce(username='sreitz@globaltiesus.org.squad', password='5TeveSharesHisPasswordWithATest!', security_token='FaXEITsepoRLxFqxZ4MXSGtL6', domain='test')
print(sf.query_all("SELECT Id, Email FROM Contact WHERE LastName = 'Jones'"))

# print(sf.query("SELECT Id, UserId FROM UserDevice"))