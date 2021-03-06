import numpy as np 
import pandas as pd 
import re
import math
def main():
	df = pd.read_csv("twcs.csv")
	print(list(df.columns))
	data_numpy = df.to_numpy()
	customer_service = {}
	# print(df["inbound"])
	tweet_dic = {}

	q_and_a = []
	Question_answer = []
	for line in data_numpy:
		cleaned_text_at = re.sub(r'@[A-Za-z0-9]+','',line[4])
		cleaned_text_ulr = re.sub('https?://[A-Za-z0-9./]+','',cleaned_text_at)
		tweet_dic[line[0]] = cleaned_text_ulr
		if(line[2]):
			q_and_a.append((line[0],line[5]))
	for pair in q_and_a:
		Q = pair[0]
		A = ""
		if(isinstance(pair[1],float)):
			continue
		answer = pair[1].split(",")
		if(len(answer)>1):
			for a in answer:
				if(int(a) in tweet_dic):
					A+=tweet_dic[int(a)]+"||"
		else:
			if(int(answer[0]) in tweet_dic):
				A+= tweet_dic[int(answer[0])]+"||"
		Question_answer.append((tweet_dic[int(Q)],A))
	# print(Question_answer)
	write_result(Question_answer)
def write_result(Question_answer):
	with open("tw_Q&A.txt","w",encoding="utf8") as file:
		for conversation in Question_answer:
			file.write(conversation[0]+"\n")
			file.write(conversation[1]+"\n")
			file.write("\n")


main()