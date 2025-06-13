from prettytable import PrettyTable
from prettytable import DOUBLE_BORDER

def table_maker(hit_miss, page_fault, history, refstring, page_frames):
    table = PrettyTable()
    table.set_style(DOUBLE_BORDER)
    for i in range(0,len(refstring.split(','))):
        table.add_column(refstring.split(',')[i], history[i])
    table.add_row([""]*len(refstring.split(',')), divider=True)
    table.add_row(hit_miss)
    print(f"Page Reference: {refstring} \t\t No. of Page Frames: {page_frames}\n")
    print(table)
    print(f"\nPage Fault: {page_fault}\n\n")
    
    
class PageReplacement:
    def __init__(self, frames):
        self.frame_list = []
        self.hit_miss = []
        self.frames = frames
        self.page_fault = 0
        self.history = []
    
    def least_recently_used(self, refstring):
        lru_idx = 0
        self.page_fault = 0
        self.hit_miss = []
        lru_use = {}
        self.history = []
        self.frame_list = []
        for page in refstring.split(','):
            if page not in self.frame_list:
                self.hit_miss.append('Miss')
                self.page_fault = self.page_fault + 1
                if len(self.frame_list) < self.frames:
                    self.frame_list.append(page)
                else:
                    lru_page = min(lru_use, key = lru_use.get)
                    lru_use.pop(lru_page)
                    self.frame_list = [page if x==lru_page else x for x in self.frame_list]
            else:
                self.hit_miss.append('Hit')
            lru_use[page] = lru_idx
            lru_idx = lru_idx + 1
            self.history.append([x for x in self.frame_list] + ["_"] * (self.frames - len(self.frame_list)))
        print("LEAST RECENTLY USED")
        table_maker(hit_miss=self.hit_miss, history=self.history, page_fault=self.page_fault, refstring=refstring, page_frames=self.frames)   
    
    def least_frequently_used(self, refstring):
        frequency = {}
        self.page_fault = 0
        self.hit_miss = []
        self.history = []
        self.frame_list = []
        for page in refstring.split(","):
            if page not in self.frame_list:
                self.hit_miss.append("Miss")
                self.page_fault = self.page_fault + 1
                if(len(self.frame_list) < self.frames):
                    self.frame_list.append(page)
                else:
                    lfu_page = min(frequency, key = frequency.get)
                    frequency.pop(lfu_page)
                    self.frame_list = [page if x == lfu_page else x for x in self.frame_list]
            else:
                self.hit_miss.append("Hit")
            frequency[page] = frequency.get(page, 0) + 1
            self.history.append([x for x in self.frame_list] + ["_"] * (self.frames - len(self.frame_list)))
        print("LEAST FREQUENTLY USED")
        table_maker(hit_miss=self.hit_miss, history=self.history, page_fault=self.page_fault, refstring=refstring, page_frames=self.frames)  
    
    def first_in_first_out(self, refstring):
        self.page_fault = 0
        self.hit_miss = []
        self.history = []
        self.frame_list = []
        fifo_idx = 0
        for page in refstring.split(","):
            if page not in self.frame_list:
                self.hit_miss.append("Miss")
                self.page_fault = self.page_fault + 1
                if(len(self.frame_list) < self.frames):
                    self.frame_list.append(page)
                else:
                    self.frame_list[fifo_idx] = page
                    fifo_idx = (fifo_idx + 1) % self.frames
            else:
                self.hit_miss.append("Hit")
            self.history.append([x for x in self.frame_list] + ["_"] * (self.frames - len(self.frame_list)))
        print("FIRST IN FIRST OUT")
        table_maker(hit_miss=self.hit_miss, history=self.history, page_fault=self.page_fault, refstring=refstring, page_frames=self.frames)  
   
def main():
    page_replacer = PageReplacement(4)
    page_replacer.least_recently_used("7,0,1,2,0,3,0,4,2,3,0,3,2,3")
    page_replacer.least_frequently_used("7,0,1,2,0,3,0,4,2,3,0,3,2,3")
    page_replacer.first_in_first_out("7,0,1,2,0,3,0,4,2,3,0,3,2,3")
    
    
if __name__ == "__main__":
    print("hello world")
    main()