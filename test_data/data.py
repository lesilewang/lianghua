#!/usr/bin/env python
#-*- coding: UTF-8 -*-
import sys,os,time,datetime,struct,zipfile,gzip

class DMD:
    def __init__(self):
        self.TradingDay = ""
        self.InstrumentID = ""
        self.ExchangeID = ""
        self.ExchangeInstID = ""
        self.LastPrice = 0.0
        self.PreSettlementPrice = 0.0
        self.PreClosePrice = 0.0
        self.PreOpenInterest = 0.0
        self.OpenPrice = 0.0
        self.HighestPrice = 0.0
        self.LowestPrice = 0.0
        self.Volume = 0
        self.Turnover = 0.0
        self.OpenInterest = 0.0
        self.ClosePrice = 0.0
        self.SettlementPrice = 0.0
        self.UpperLimitPrice = 0.0
        self.LowerLimitPrice = 0.0
        self.PreDelta = 0.0
        self.CurrDelta = 0.0
        self.UpdateTime = ""
        self.UpdateMillisec = 0
        self.BidPrice1 = 0.0
        self.BidVolume1 = 0
        self.AskPrice1 = 0.0
        self.AskVolume1 = 0
        self.BidPrice2 = 0.0
        self.BidVolume2 = 0
        self.AskPrice2 = 0.0
        self.AskVolume2 = 0
        self.BidPrice3 = 0.0
        self.BidVolume3 = 0
        self.AskPrice3 = 0.0
        self.AskVolume3 = 0
        self.BidPrice4 = 0.0
        self.BidVolume4 = 0
        self.AskPrice4 = 0.0
        self.AskVolume4 = 0
        self.BidPrice5 = 0.0
        self.BidVolume5 = 0
        self.AskPrice5 = 0.0
        self.AskVolume5 = 0
        self.AveragePrice = 0.0

def strDMD1(dmd):
    return " ".join([dmd.InstrumentID,dmd.TradingDay,dmd.UpdateTime[0:8],str(dmd.UpdateMillisec).zfill(3),str(dmd.LastPrice),str(dmd.Volume).ljust(6),str(dmd.diffvol).rjust(3),str(dmd.OpenInterest).rjust(6),str(dmd.diffOI).rjust(6),str(dmd.AskPrice1),str(dmd.AskVolume1).rjust(3),str(dmd.BidPrice1),str(dmd.BidVolume1).rjust(3),str(dmd.AskVolume2),str(dmd.Turnover),str(dmd.AveragePrice),str(dmd.SettlementPrice),str(dmd.UpperLimitPrice),str(dmd.LowerLimitPrice)  ])
def strDMD2(dmd):
    if dmd == None : return ""
    x = time.localtime(dmd.timestamp/1000000)
    t = time.strftime('%Y%m%d %H:%M:%S',x)
    strTimestamp = t+"."+str(dmd.timestamp % 1000000)
    #strAvgPri = str(round(dmd.avgpri/300,2)).rjust(3)
    strAvgPri = str(round(dmd.avgpri/5,2)).rjust(3)
    if dmd.AskPrice5 > 999999 : dmd.AskPrice5 = 0
    if dmd.AskPrice4 > 999999 : dmd.AskPrice4 = 0
    if dmd.AskPrice3 > 999999 : dmd.AskPrice3 = 0
    if dmd.AskPrice2 > 999999 : dmd.AskPrice2 = 0
    if dmd.AskPrice1 > 999999 : dmd.AskPrice1 = 0
    if dmd.BidPrice5 > 999999 : dmd.BidPrice5 = 0
    if dmd.BidPrice4 > 999999 : dmd.BidPrice4 = 0
    if dmd.BidPrice3 > 999999 : dmd.BidPrice3 = 0
    if dmd.BidPrice2 > 999999 : dmd.BidPrice2 = 0
    if dmd.BidPrice1 > 999999 : dmd.BidPrice1 = 0
    
    ngapdiff = dmd.AskPrice1 - dmd.BidPrice1
    strGapDiff = str(ngapdiff)
    #return " ".join([dmd.InstrumentID,dmd.TradingDay,dmd.UpdateTime[0:8],str(dmd.UpdateMillisec).zfill(3),str(dmd.LastPrice),str(dmd.Volume).ljust(6),str(dmd.diffvol).rjust(3),str(dmd.OpenInterest).rjust(6),str(dmd.diffOI).rjust(6),str(dmd.AskPrice1),str(dmd.AskVolume1).rjust(3),str(dmd.BidPrice1),str(dmd.BidVolume1).rjust(3),str(dmd.AskPrice2),str(dmd.AskVolume2).rjust(3),str(dmd.BidPrice2),str(dmd.BidVolume2).rjust(3),str(dmd.Turnover),str(dmd.AveragePrice),str(dmd.SettlementPrice),str(dmd.UpperLimitPrice),str(dmd.LowerLimitPrice)  ])
    #return " ".join([dmd.InstrumentID,dmd.TradingDay,dmd.UpdateTime[0:8],str(dmd.UpdateMillisec).zfill(3),str(dmd.LastPrice),str(dmd.Volume).ljust(6),str(dmd.diffvol).rjust(3),str(dmd.OpenInterest).rjust(6),str(dmd.diffOI).rjust(6),str(dmd.AskPrice1),str(dmd.AskVolume1).rjust(3),str(dmd.BidPrice1),str(dmd.BidVolume1).rjust(3),str(dmd.AskPrice2),str(dmd.AskVolume2).rjust(3),str(dmd.BidPrice2),str(dmd.BidVolume2).rjust(3),str(dmd.AskPrice3),str(dmd.AskVolume3).rjust(3),str(dmd.BidPrice3),str(dmd.BidVolume3).rjust(3) ])
    if dmd.BidPrice5 > 0 :
        return " ".join([dmd.InstrumentID,dmd.UpdateTime[0:8],str(dmd.UpdateMillisec)[0:1].zfill(1),str(dmd.LastPrice),str(dmd.diffvol).ljust(6),"|",str(dmd.AskPrice5),str(dmd.AskVolume5).rjust(3),str(dmd.AskPrice4),str(dmd.AskVolume4).rjust(3),str(dmd.AskPrice3),str(dmd.AskVolume3).rjust(3),str(dmd.AskPrice2),str(dmd.AskVolume2).rjust(3),str(dmd.AskPrice1),str(dmd.AskVolume1).rjust(3),"||",str(dmd.BidPrice1),str(dmd.BidVolume1).rjust(3),str(dmd.BidPrice2),str(dmd.BidVolume2).rjust(3),str(dmd.BidPrice3),str(dmd.BidVolume3).rjust(3),str(dmd.BidPrice4),str(dmd.BidVolume4).rjust(3),str(dmd.BidPrice5),str(dmd.BidVolume5).rjust(3),"|"+strAvgPri+" "+strGapDiff])
    else :
        return " ".join([dmd.InstrumentID,dmd.UpdateTime[0:8],str(dmd.UpdateMillisec)[0:1].zfill(1),str(dmd.LastPrice),str(dmd.diffvol).ljust(3),"|",str(dmd.AskPrice1),str(dmd.AskVolume1).rjust(3),"||",str(dmd.BidPrice1),str(dmd.BidVolume1).rjust(3),"|"+strAvgPri+" "+strGapDiff])
def getDayData(Data,InstrumentID,path ="./"):
    if os.path.exists(path+"/"+Data+".zip")== False:
        print 'the  zipfile is not exist'
        ttp = path+"/"+Data+".zip"
        print ttp
        return []
    fz = zipfile.ZipFile(path+"/"+Data+".zip","r")

    #fp= path+"/"+Data+".zip"
    #print fp
    
    namelist = fz.namelist() ; 
   # print namelist
    if InstrumentID not in namelist :
        return []
        print 'InstrumentID not in namelist'
    #fz = gzip.GzipFile(Data+".tgz","r")
    itemsize = 416 # 392
    lines = fz.read(InstrumentID)
    nCnt = len(lines) / itemsize

    preVol = 0; preOI = 0 ; preTurnover = 0 ;tmsp = 0
    l_data = []

    for i in range(0,nCnt):
        dmd = DMD()
        t_t = lines[i*itemsize:(i+1)*itemsize]
        #s_r = (dmd.TradingDay,dmd.InstrumentID,dmd.ExchangeID,dmd.ExchangeInstID,dmd.LastPrice,dmd.PreSettlementPrice,dmd.PreClosePrice,dmd.PreOpenInterest,dmd.OpenPrice,dmd.HighestPrice,dmd.LowestPrice,dmd.Volume,dmd.Turnover,dmd.OpenInterest,dmd.ClosePrice,dmd.SettlementPrice,dmd.UpperLimitPrice,dmd.LowerLimitPrice,dmd.PreDelta,dmd.CurrDelta,dmd.UpdateTime,dmd.UpdateMillisec,dmd.BidPrice1,dmd.BidVolume1,dmd.AskPrice1,dmd.AskVolume1,dmd.BidPrice2,dmd.BidVolume2,dmd.AskPrice2,dmd.AskVolume2,dmd.BidPrice3,dmd.BidVolume3,dmd.AskPrice3,dmd.AskVolume3,dmd.BidPrice4,dmd.BidVolume4,dmd.AskPrice4,dmd.AskVolume4,dmd.BidPrice5,dmd.BidVolume5,dmd.AskPrice5,dmd.AskVolume5,dmd.AveragePrice)
        #s_r = struct.unpack('9s31s9s31sdddddddidddddddd9sididididididididididid',t_t)
        dmd.timestamp,dmd.TradingDay,dmd.InstrumentID,dmd.ExchangeID,dmd.ExchangeInstID,dmd.LastPrice,dmd.PreSettlementPrice,dmd.PreClosePrice,dmd.PreOpenInterest,dmd.OpenPrice,dmd.HighestPrice,dmd.LowestPrice,dmd.Volume,dmd.Turnover,dmd.OpenInterest,dmd.ClosePrice,dmd.SettlementPrice,dmd.UpperLimitPrice,dmd.LowerLimitPrice,dmd.PreDelta,dmd.CurrDelta,dmd.UpdateTime,dmd.UpdateMillisec,dmd.BidPrice1,dmd.BidVolume1,dmd.AskPrice1,dmd.AskVolume1,dmd.BidPrice2,dmd.BidVolume2,dmd.AskPrice2,dmd.AskVolume2,dmd.BidPrice3,dmd.BidVolume3,dmd.AskPrice3,dmd.AskVolume3,dmd.BidPrice4,dmd.BidVolume4,dmd.AskPrice4,dmd.AskVolume4,dmd.BidPrice5,dmd.BidVolume5,dmd.AskPrice5,dmd.AskVolume5,dmd.AveragePrice, dmd.TThostFtdcDateType = struct.unpack('q9s31s9s31sdddddddidddddddd9sididididididididididid16s',t_t)
        dmd.TradingDay = dmd.TradingDay[0:8]
        dmd.UpdateTime = dmd.UpdateTime[0:8] 
        dmd.InstrumentID = InstrumentID#sys.argv[2] #dmd.InstrumentID.lstrip("\0")
#        if(temp<200):
#            print dmd.TradingDay,dmd.UpdateTime
#            temp += 1
        
        if dmd.AskPrice5 > 999999 : dmd.AskPrice5 = 0
        if dmd.AskPrice4 > 999999 : dmd.AskPrice4 = 0
        if dmd.AskPrice3 > 999999 : dmd.AskPrice3 = 0
        if dmd.AskPrice2 > 999999 : dmd.AskPrice2 = 0
        if dmd.AskPrice1 > 999999 : dmd.AskPrice1 = 0
        if dmd.BidPrice5 > 999999 : dmd.BidPrice5 = 0
        if dmd.BidPrice4 > 999999 : dmd.BidPrice4 = 0
        if dmd.BidPrice3 > 999999 : dmd.BidPrice3 = 0
        if dmd.BidPrice2 > 999999 : dmd.BidPrice2 = 0
        if dmd.BidPrice1 > 999999 : dmd.BidPrice1 = 0
        if dmd.LastPrice > 999999 : dmd.LastPrice = 0
            
        #print s_r
        #print  dmd.TradingDay + " ." + dmd.InstrumentID[0:6] + " "+ str(dmd.LastPrice)
        #print dmd.TradingDay + " "+ dmd.InstrumentID
        #print " ".join([s_r[0],s_r[1],str(s_r[4])])
        #str_show = s_r[0]+" "+s_r[1]+" "+str(s_r[4])+" "+str(s_r[11])+" "+str(s_r[12])+" "+str(s_r[13])+" "+str(s_r[20])+" "+str(s_r[21])+" "+str(s_r[22])+" "+str(s_r[23])+" "+str(s_r[24])+" "+str(s_r[25])+" "+str(s_r[29])+" "+str(s_r[42])+" "
        #print s_r[0]+" "+s_r[1]+" "+str(s_r[4])+" "+str(s_r[11])+" "+str(s_r[12])+" "+str(s_r[13])+" "+str(s_r[16])+" "+str(s_r[17])+" "+
        #print str_show
        if tmsp == 0:
            tmsp =  dmd.AskVolume2
        #dmd.timestamp = dmd.AskVolume2
        #print "ddddddddddddddddddd"
        #print " ".join([dmd.InstrumentID,dmd.TradingDay,dmd.UpdateTime[0:8],str(dmd.UpdateMillisec).zfill(3),str(dmd.LastPrice),str(dmd.Volume).ljust(6),str(dmd.Volume-preVol).rjust(3),str(dmd.OpenInterest).rjust(6),str(dmd.OpenInterest-preOI).rjust(6),str(dmd.AskPrice1),str(dmd.AskVolume1).rjust(3),str(dmd.BidPrice1),str(dmd.BidVolume1).rjust(3),str(dmd.AskVolume2),str(dmd.Turnover),str(dmd.AveragePrice),str(dmd.SettlementPrice),str(dmd.UpperLimitPrice),str(dmd.LowerLimitPrice)  ])

        dmd.diffvol = dmd.Volume - preVol
        dmd.diffOI = dmd.OpenInterest - preOI
        dmd.diffTurnover = dmd.Turnover - preTurnover
        preTurnover = dmd.Turnover
        if dmd.diffvol == 0 : dmd.avgpri = 0
        else : dmd.avgpri = dmd.diffTurnover / dmd.diffvol
        preVol = dmd.Volume ; preOI = dmd.OpenInterest ; #tmsp =  dmd.AskVolume2
        l_data += [dmd]
    #print  i   
    return l_data
#getDayData(sys.argv[1],sys.argv[2])

#exit(0)



#current day date
#dt = datetime.datetime.strptime(date_t,"%Y%m%d")
#time.localtime(time.time())
#dt = time.strftime('%Y%m%d',time.localtime(time.time()))

#filelist = os.listdir(dt)
#print filelist
#for f_ism in filelist :
if 0:
    filename = dt + "/"+f_ism
    f = open(filename,"rb")
    #while(s=f.read(392)):
    while True:
        s = f.read(392)
        if not s : break;
        dmd = DMD()
        #(dmd.TradingDay,dmd.InstrumentID)=struct.unpack('9s31s9s31s',s)
        s_r = (dmd.TradingDay,dmd.InstrumentID,dmd.ExchangeID,dmd.ExchangeInstID,dmd.LastPrice,dmd.PreSettlementPrice,dmd.PreClosePrice,dmd.PreOpenInterest,dmd.OpenPrice,dmd.HighestPrice,dmd.LowestPrice,dmd.Volume,dmd.Turnover,dmd.OpenInterest,dmd.ClosePrice,dmd.SettlementPrice,dmd.UpperLimitPrice,dmd.LowerLimitPrice,dmd.PreDelta,dmd.CurrDelta,dmd.UpdateTime,dmd.UpdateMillisec,dmd.BidPrice1,dmd.BidVolume1,dmd.AskPrice1,dmd.AskVolume1,dmd.BidPrice2,dmd.BidVolume2,dmd.AskPrice2,dmd.AskVolume2,dmd.BidPrice3,dmd.BidVolume3,dmd.AskPrice3,dmd.AskVolume3,dmd.BidPrice4,dmd.BidVolume4,dmd.AskPrice4,dmd.AskVolume4,dmd.BidPrice5,dmd.BidVolume5,dmd.AskPrice5,dmd.AskVolume5,dmd.AveragePrice)
        s_r = struct.unpack('9s31s9s31sdddddddidddddddd9sididididididididididid',s)

        print s_r
    break

#close(sys.stdout)
#sys.stdout.close()

if __name__=="__main__":
    strdata = sys.argv[1]
    strInsLeft = sys.argv[2]
    #strInsRight = sys.argv[3]
    l = getDayData(strdata,strInsLeft)   
    for i in l : 
        print " ".join([str(i.InstrumentID),str(i.TradingDay),str(i.UpdateTime)[0:8],str(i.UpdateMillisec),str(i.LastPrice),str(i.Volume),str(i.AskPrice1),str(i.AskVolume1),str(i.BidPrice1),str(i.BidVolume1),str(i.Turnover)])



    
