num_streams = int(input())
stream_list = [] # the value of the num in the list repersent the flow of the rivers, the index of the list repersent the river number. Indexes auto update from left to right so the streams will always be the right number
for interations in range(0,num_streams):
  flow = int(input())
  stream_list.append(flow)

while True:
  action = int(input())
  if action == 99:
    stream_index = int(input())
    flow_percent = int(input())
    #Makes the new stream value 100-X percent of the original stream
    stream_list.insert(stream_index, stream_list[stream_index-1]*((100-flow_percent)/100))
    #Make the original stream value X percent of itself
    stream_list[stream_index-1] = (stream_list[stream_index-1])*(flow_percent/100) 
  
  
  elif action == 88:
    stream_index = int(input())
    stream_list[stream_index] = stream_list[stream_index] + stream_list[stream_index-1]
    del stream_list[stream_index-1]
  elif action == 77:
    break 
  

temp_str = ""

for items in stream_list:
  temp_str += (str(round(items))+" ")

print(temp_str)
