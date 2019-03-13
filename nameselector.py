import json
import codecs
import argparse

class nameselector:
	def __init__(self,cpath,tpath,opath):
		self.cluster_dataset = {}
		self.tweet_dataset = {}
		self.cluter_to_name = {}
		self.cpath = cpath
		self.tpath = tpath
		self.opath = opath


	def read_cluster(self,path):
		with codecs.open(path,"r","utf-8-sig") as f:
			for line in f:
				cluster = json.loads(line)
				cid =  cluster["id"]
				doc =  cluster["doc"]
				self.cluster_dataset[cid] = doc

	def read_tweet(self,path):
		with codecs.open(path, "r","utf-8-sig") as f:
			for line in f:
				d = json.loads(line)
				tid = d[u'id']
				ttype = d["type"]
				tlocation = d["location"]
				self.tweet_dataset[tid] = {"type":ttype, "location":tlocation}
	def generate_name(self,clus_doc):
		voting = {}
		for d in clus_doc:
			candidate = self.tweet_dataset[d]["type"] +" in "+ self.tweet_dataset[d]["location"]
			if candidate not in voting:
				voting[candidate]  = 0
			voting[candidate] += 1
		return sorted(list(voting.items()),key=lambda x:x[1],reverse=True)[0][0]


	def run(self):
		self.read_cluster(self.cpath)
		self.read_tweet(self.tpath)
		for c in self.cluster_dataset:
			cname = self.generate_name(self.cluster_dataset[c])
			self.cluter_to_name[c] = cname
		with codecs.open(self.opath,"w","utf-8-sig") as f:
			for i in self.cluster_dataset:
				clusters = {"id": i, "cluster_name": self.cluter_to_name[i], "doc": self.cluster_dataset[i]}
				f.write(json.dumps(clusters,ensure_ascii=False) + "\n")


def args_parse():
	# construct the argument parse and parse the arguments
	ap = argparse.ArgumentParser()
	ap.add_argument("-c", required=True,metavar='cluster_file', help="path to input cluster file")
	ap.add_argument("-t", required=True,metavar='original_file', help="path to input raw file")
	ap.add_argument("-o", required=True, metavar='output_file',help="path to output")
	args = vars(ap.parse_args())
	return args

def main():
	args = args_parse()
	cpath = args["c"]
	tpath = args["t"]
	opath = args["o"]
	select = nameselector(cpath,tpath,opath)
	select.run()

if __name__ == '__main__':
  main()