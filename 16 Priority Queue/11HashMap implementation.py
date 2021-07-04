class HashMap:
    def __init__(self):
        self.size=0
        self.buckets=[[] for i in range(4)]
    class HMNode:
        def __init__(self, key, value):
            self.key=key
            self.value=value
    def put(self,key,value):
        bucket_index=self.hashfun(key)
        data_index=self.getIndexWithInBucket(key,bucket_index)
        if data_index==-1:
            self.buckets[bucket_index].append(self.HMNode(key,value))
            self.size+=1
        else:
            self.buckets[bucket_index][data_index].value=value
        lamda=self.size/len(self.buckets)
        if lamda>2.0:
            self.rehash()
    def rehash(self):
        old_bucket_list=self.buckets
        self.buckets=[[] for i in range(len(old_bucket_list)*2)]
        self.size=0
        for i in range(len(old_bucket_list)):
            for node in old_bucket_list[i]:
                self.put(node.key,node.value)
    def contains(self,key):
        bucket_index = self.hashfun(key)
        data_index = self.getIndexWithInBucket(key, bucket_index)
        if data_index == -1:
            return False
        else:
            return True
    def get(self,key):
        bucket_index = self.hashfun(key)
        data_index = self.getIndexWithInBucket(key, bucket_index)
        if data_index == -1:
            return None
        else:
            return self.buckets[bucket_index][data_index].value
    def remove(self,key):
        bucket_index = self.hashfun(key)
        data_index = self.getIndexWithInBucket(key, bucket_index)
        if data_index == -1:
            return None
        else:
            self.size-=1
            node=self.buckets[bucket_index].pop(data_index)
            str1=node.key+"@"+str(node.value)
            return str1
    def KeySet(self):
        keys=[]
        for buk in range(len(self.buckets)):
            for node in self.buckets[buk]:
                keys.append(node.key)
        return keys
    def size_HM(self):
        return self.size
    def hashfun(self,key):
        hc=hash(key)
        return abs(hc)%len(self.buckets)
    def getIndexWithInBucket(self,key,bucket_index):
        di=0
        for node in self.buckets[bucket_index]:
            if node.key==key:
                return di
            else:
                di+=1
        return -1
    def display(self):
        for i in range(len(self.buckets)):
            print("Bucket{} ".format(i),end=" ")
            for node in self.buckets[i]:
                print(node.key,"@",node.value,end=" ")
            print()

    def fun(self):
        self.put("India",135)
        self.put("aus",5)
        self.put("Canada",3)
        self.display()
        print(self.get("China"))
        print(self.remove("aus"))
        print(self.get("aus"))
        print(self.contains("US"))
        self.put("US",10)
        self.put("UK",20)
        print(self.remove("US"))
        print(self.contains("US"))
        self.put("Pak",80)
        self.put("China",200)
        self.display()
        self.put("Utopia",0)
        self.display()
        self.put("Nigeria",3)
        self.display()
        self.put("India",138)
        self.display()
        self.put("Sweden",1)
        self.display()
        self.put("finland",20)
        self.display()
hm=HashMap()
hm.fun()



