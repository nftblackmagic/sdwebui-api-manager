import uuid
import queue
import threading
import time
from app.api import api 

current_request = {}
final_results = {}

class QueueMonitor:
    def __init__(self, q):
        self.q = q
        self.monitor_thread = threading.Thread(target=self.monitor_queue, daemon=True)
        self.monitor_thread.start()

    def get_queue_size(self):
        return self.q.qsize()

    def monitor_queue(self):
        while True:
            current_size = self.get_queue_size()
            if current_size > 0:
                self.queue_has_items()
            time.sleep(1)  # check the queue every second

    def queue_has_items(self):
        print(f"Queue has items. Current size: {self.get_queue_size()}")
        self.callback_function()

    def callback_function(self):
        start_process_queue()


requests_queue = queue.Queue(20)

# Create a QueueMonitor object with the Queue
monitor = QueueMonitor(requests_queue)

def start_process_queue():
  global current_request
  global final_results
  if((current_request.get("status") != "pending") and (current_request.get("status") != "processing")):
      if not requests_queue.empty():
        current_request = requests_queue.get()
        current_request["status"] = "processing"
        print ("current_request is processing", current_request.get("request_id"), current_request.get("status"))
        if(current_request.get("type") == "txt2img"):
            res = api.txt2img(current_request.get("payload"))
            final_request = current_request
            final_request["status"] = "done"
            final_request["result"] = res
            current_request["status"] = "done"
            final_results[final_request.get("request_id")] = final_request
            print("request is complete", final_request.get("request_id"), final_request.get("status"))
        if(current_request.get("type") == "img2img"):
            res = api.img2img(current_request.get("payload"))
            final_request = current_request
            final_request["status"] = "done"
            final_request["result"] = res
            current_request["status"] = "done"
            final_results[final_request.get("request_id")] = final_request
            print("request is complete", final_request.get("request_id"), final_request.get("status"))

def add_req_queue(payload, type):
    filter_data = {}

    for k,v in payload.items():
        if payload[k] != None:
            filter_data[k] = v
    
    request_id = str(uuid.uuid4())
    temp_request = {
        "type": type,
        "payload": filter_data,
        "request_id": request_id,
        "status": "pending"
    }
    requests_queue.put(temp_request)
    print("add request into queue, pending", request_id)
    return temp_request

def check_variable_in_queue(q, var):
    queue_as_list = list(q.queue)
    pending_requests = []
    for i in queue_as_list:
        pending_requests.append(i.get("request_id"));
    if var in pending_requests:
        print(f"{var} is in the queue.")
        return pending_requests.index(var)
    else:
        print(f"{var} is not in the queue.")
        return -1

def get_result(request_id):
    global final_results
    print("final_results", final_results.keys())
    if(request_id in final_results):
        return final_results[request_id]
    elif(request_id == current_request.get("request_id")):
        res = api.progress()
        temp_res = current_request
        temp_res["result"] = res
        return temp_res
    else:
        index = check_variable_in_queue(requests_queue, request_id)
        if(index > -1):
            return {"status": "pending", "request_id": request_id, "pending_count": index}
        else:
            return {"status": "not_found"}