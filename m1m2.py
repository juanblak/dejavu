import warnings
import json
warnings.filterwarnings("ignore")

from dejavu import Dejavu


from line_profiler import LineProfiler #running time

# load config from a JSON file (or anything outputting a python dictionary)
with open("dejavu.cnf.SAMPLE") as f:
    config = json.load(f)

if __name__ == '__main__':

	# create a Dejavu instance
	djv = Dejavu(config)

	lp = LineProfiler()
	lp_wrapper = lp(djv.fingerprint_directory)
	lp_wrapper("music", [".mp3"]) # file directory to fingerprint
	lp.print_stats()
	# start = time.time()
	# djv.fingerprint_directory("music", [".mp3"])
	# end=time.time()
	# r_time=end-start
	# print('Running time: %s Seconds' % r_time)

	print(djv.db.get_num_fingerprints())


