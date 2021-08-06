import discord
async def fetchannel(message):
  messages = await message.channel.history(limit=None).flatten()
  context = [str(i.content) for i in messages]
  with open("file.txt", "w") as output:
    output.write(convertstring(context))
def convertstring(list):
  
  list.reverse()
  changelist=[str(i).replace("'","").replace("'","").replace("(","").replace(")","").lstrip().replace(",","").replace("!export","").replace("List show all","").replace("successfully add","").replace("List add","") for i in list]
  
  listostring = "\n".join(changelist)
  return listostring