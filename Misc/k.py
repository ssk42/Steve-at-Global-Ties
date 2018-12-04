 checkpoints_parsed= json.dump(response.json())
 chkpts_data=checkpoints_parsed['tasks']
 chkpts_data=open('chkpts.csv','w')
 csvwriter= csv.writer(chkpts_data)
 count=0
 for chkpt in chkpts_data:
    if count==0:
        header=chkpt.keys()
        csvwriter.writerow(header)
        count+=1
    csvwriter.writerow(chkpt.values())
 chkpts_data.close()
with open('data.txt', 'w') as f:
  #json.dump((response.json()), f, ensure_ascii=False,indent=4, sort_keys=True)



# 9 people are currently in space.
