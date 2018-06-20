#!/usr/bin/env python
#-*- coding: UTF-8 -*-
import sys,os,time,datetime,struct,zipfile,gzip
import csv
from compiler.pycodegen import EXCEPT

class DepthMarketDataField:
    def __init__(self):
        #交易日
        self.TradingDay = "";
        #结算组代码
        self.SettlementGroupID = "";
        #结算编号
        self.SettlementID = "";
        #最新价
        self.LastPrice = 0.0;
        #昨结算
        self.PreSettlementPrice = 0.0;
        #昨收盘
        self.PreClosePrice = 0.0;
        #昨持仓量
        self.PreOpenInterest = 0.0;
        #今开盘
        self.OpenPrice = 0.0;
        #最高价
        self.HighestPrice = 0.0;
        #最低价
        self.LowestPrice = 0.0;
        #数量
        self.Volume = 0;
        #成交金额
        self.Turnover = 0.0;
        #持仓量
        self.OpenInterest = 0.0;
        #今收盘
        self.ClosePrice = 0.0;
        #今结算
        self.SettlementPrice = 0.0;
        #涨停板价
        self.UpperLimitPrice = 0.0;
        #跌停板价
        self.LowerLimitPrice = 0.0;
        #昨虚实度
        self.PreDelta = 0.0;
        #今虚实度
        self.CurrDelta = 0.0;
        #最后修改时间
        self.UpdateTime = "";
        #最后修改毫秒
        self.UpdateMillisec = 0;
        #合约代码
        self.InstrumentID = "";
        #申买价一 
        self.BidPrice1 = 0.0;
        #申买量一
        self.BidVolume1 = 0;
        #申卖价一
        self.AskPrice1 = 0.0;
        #申卖量一
        self.AskVolume1 = 0;
        #申买价二
        self.BidPrice2 = 0.0;
        #申买量二
        self.BidVolume2 = 0;
        #申卖价二
        self.AskPrice2 = 0.0;
        #申卖量二
        self.AskVolume2 = 0;
        #申买价三
        self.BidPrice3 = 0.0;
        #申买量三
        self.BidVolume3 = 0;
        #申卖价三
        self.AskPrice3 = 0.0;
        #申卖量三
        self.AskVolume3 = 0;
        #申买价四
        self.BidPrice4 = 0.0;
        #申买量四
        self.BidVolume4 = 0;
        #申卖价四
        self.AskPrice4 = 0.0;
        #申卖量四
        self.AskVolume4 = 0;
        #申买价五
        self.BidPrice5 = 0.0;
        #申买量五
        self.BidVolume5 = 0;
        #申卖价五
        self.AskPrice5 = 0.0;
        #申卖量五
        self.AskVolume5 = 0;
        
        self._idx = 0;#char8
        #时间戳
        self.timestamp = 0;#char8
#         self.TradingDay = ""
#         self.InstrumentID = ""
#         self.ExchangeID = ""
#         self.ExchangeInstID = ""
#         self.LastPrice = 0.0
#         self.PreSettlementPrice = 0.0
#         self.PreClosePrice = 0.0
#         self.PreOpenInterest = 0.0
#         self.OpenPrice = 0.0
#         self.HighestPrice = 0.0
#         self.LowestPrice = 0.0
#         self.Volume = 0
#         self.Turnover = 0.0
#         self.OpenInterest = 0.0
#         self.ClosePrice = 0.0
#         self.SettlementPrice = 0.0
#         self.UpperLimitPrice = 0.0
#         self.LowerLimitPrice = 0.0
#         self.PreDelta = 0.0
#         self.CurrDelta = 0.0
#         self.UpdateTime = ""
#         self.UpdateMillisec = 0
#         self.BidPrice1 = 0.0
#         self.BidVolume1 = 0
#         self.AskPrice1 = 0.0
#         self.AskVolume1 = 0
#         self.BidPrice2 = 0.0
#         self.BidVolume2 = 0
#         self.AskPrice2 = 0.0
#         self.AskVolume2 = 0
#         self.BidPrice3 = 0.0
#         self.BidVolume3 = 0
#         self.AskPrice3 = 0.0
#         self.AskVolume3 = 0
#         self.BidPrice4 = 0.0
#         self.BidVolume4 = 0
#         self.AskPrice4 = 0.0
#         self.AskVolume4 = 0
#         self.BidPrice5 = 0.0
#         self.BidVolume5 = 0
#         self.AskPrice5 = 0.0
#         self.AskVolume5 = 0
#         self.AveragePrice = 0.0
'''
///深度市场行情
struct CFfexFtdcDepthMarketDataField
{
    ///交易日
    TFfexFtdcDateType    TradingDay;typedef char TFfexFtdcDateType[9];
    ///结算组代码
    TFfexFtdcSettlementGroupIDType    SettlementGroupID;typedef char TFfexFtdcSettlementGroupIDType[9];
    ///结算编号
    TFfexFtdcSettlementIDType    SettlementID;typedef int TFfexFtdcSettlementIDType;
    ///最新价
    TFfexFtdcPriceType    LastPrice;typedef double TFfexFtdcPriceType;
    ///昨结算
    TFfexFtdcPriceType    PreSettlementPrice;typedef double TFfexFtdcPriceType;
    ///昨收盘
    TFfexFtdcPriceType    PreClosePrice;typedef double TFfexFtdcPriceType;
    ///昨持仓量
    TFfexFtdcLargeVolumeType    PreOpenInterest;typedef double TFfexFtdcLargeVolumeType;
    ///今开盘
    TFfexFtdcPriceType    OpenPrice;typedef double TFfexFtdcPriceType;
    ///最高价
    TFfexFtdcPriceType    HighestPrice;typedef double TFfexFtdcPriceType;
    ///最低价
    TFfexFtdcPriceType    LowestPrice;typedef double TFfexFtdcPriceType;
    ///数量
    TFfexFtdcVolumeType    Volume;typedef int TFfexFtdcVolumeType;
    ///成交金额
    TFfexFtdcMoneyType    Turnover;typedef double TFfexFtdcMoneyType;
    ///持仓量
    TFfexFtdcLargeVolumeType    OpenInterest;typedef double TFfexFtdcLargeVolumeType;
    ///今收盘
    TFfexFtdcPriceType    ClosePrice;typedef double TFfexFtdcPriceType;
    ///今结算
    TFfexFtdcPriceType    SettlementPrice;typedef double TFfexFtdcPriceType;
    ///涨停板价
    TFfexFtdcPriceType    UpperLimitPrice;typedef double TFfexFtdcPriceType;
    ///跌停板价
    TFfexFtdcPriceType    LowerLimitPrice;typedef double TFfexFtdcPriceType;
    ///昨虚实度
    TFfexFtdcRatioType    PreDelta;typedef double TFfexFtdcRatioType;
    ///今虚实度
    TFfexFtdcRatioType    CurrDelta;typedef double TFfexFtdcRatioType;
    ///最后修改时间
    TFfexFtdcTimeType    UpdateTime;typedef char TFfexFtdcTimeType[9];
    ///最后修改毫秒
    TFfexFtdcMillisecType    UpdateMillisec;typedef int TFfexFtdcMillisecType;
    ///合约代码9s9sidddddddidddddddd9si31sdidididididididididi
    TFfexFtdcInstrumentIDType    InstrumentID;typedef char TFfexFtdcInstrumentIDType[31];
    ///申买价一
    TFfexFtdcPriceType    BidPrice1;typedef double TFfexFtdcPriceType;
    ///申买量一
    TFfexFtdcVolumeType    BidVolume1;typedef int TFfexFtdcVolumeType;
    ///申卖价一
    TFfexFtdcPriceType    AskPrice1;typedef double TFfexFtdcPriceType;
    ///申卖量一
    TFfexFtdcVolumeType    AskVolume1;typedef int TFfexFtdcVolumeType;
    ///申买价二
    TFfexFtdcPriceType    BidPrice2;typedef double TFfexFtdcPriceType;
    ///申买量二
    TFfexFtdcVolumeType    BidVolume2;typedef int TFfexFtdcVolumeType;
    ///申卖价二
    TFfexFtdcPriceType    AskPrice2;typedef double TFfexFtdcPriceType;
    ///申卖量二
    TFfexFtdcVolumeType    AskVolume2;typedef int TFfexFtdcVolumeType;
    ///申买价三
    TFfexFtdcPriceType    BidPrice3;typedef double TFfexFtdcPriceType;
    ///申买量三
    TFfexFtdcVolumeType    BidVolume3;typedef int TFfexFtdcVolumeType;
    ///申卖价三
    TFfexFtdcPriceType    AskPrice3;typedef double TFfexFtdcPriceType;
    ///申卖量三
    TFfexFtdcVolumeType    AskVolume3;typedef int TFfexFtdcVolumeType;
    ///申买价四
    TFfexFtdcPriceType    BidPrice4;typedef double TFfexFtdcPriceType;
    ///申买量四
    TFfexFtdcVolumeType    BidVolume4;typedef int TFfexFtdcVolumeType;
    ///申卖价四
    TFfexFtdcPriceType    AskPrice4;typedef double TFfexFtdcPriceType;
    ///申卖量四
    TFfexFtdcVolumeType    AskVolume4;typedef int TFfexFtdcVolumeType;
    ///申买价五
    TFfexFtdcPriceType    BidPrice5;typedef double TFfexFtdcPriceType;
    ///申买量五
    TFfexFtdcVolumeType    BidVolume5;typedef int TFfexFtdcVolumeType;
    ///申卖价五
    TFfexFtdcPriceType    AskPrice5;typedef double TFfexFtdcPriceType;
    ///申卖量五
    TFfexFtdcVolumeType    AskVolume5;typedef int TFfexFtdcVolumeType;
};

};
'''   

def getDayData(InstrumentID,path): #此处yh修改
    #fz = zipfile.ZipFile("./"+path+"/"+Data+".zip","r")
    fz= zipfile.ZipFile(path,"r")
    namelist = fz.namelist() ; #print namelist
    if InstrumentID+'.data' not in namelist :
        return []
    #fz = gzip.GzipFile(Data+".tgz","r")
    lines = fz.read(InstrumentID+'.data')
    
    #timelines = fz.read(InstrumentID+'.tm')
    
    
#     print struct.calcsize("@i9s9sidddddddidddddddd9si31sdidididididididididi")

    preOI = 272
    size = 376
    
    nCnt = (len(lines)-preOI) / size  #根据392进行分块
    nn = lines[0:preOI] #取出该位置的数据
    u,i,o,p,maxidx = struct.unpack('ii256sii',nn)
    print "==>",str(u)+' '+str(i)+'  '+str(o)+'  '+str(p)+' '+str(maxidx)
    print "==>",str(p)+' '+str(maxidx),str(nCnt)
    #xCnt = (len(timelines)-preOI) / 8  #根据392进行分块
    #print str(nCnt)#+' '+str(xCnt)

    maxidx = 10
    l_data = []
#     g=0
    for i in range(0,100):
        dmd = DepthMarketDataField()
        t_t = lines[preOI+i*size:preOI+(i+1)*size] #取出该位置的数据
        #time_t = timelines[preOI+i*8:preOI+(i+1)*8]
        
        #dmd.timestamp = struct.unpack('q',time_t)
        dmd.TradingDay,dmd.InstrumentID, dmd.LastPrice,dmd.PreSettlementPrice,dmd.PreClosePrice,dmd.PreOpenInterest, \
        dmd.OpenPrice,dmd.HighestPrice,dmd.LowestPrice,dmd.Volume,dmd.Turnover,dmd.OpenInterest,\
        dmd.ClosePrice,dmd.SettlementPrice,dmd.UpperLimitPrice,dmd.LowerLimitPrice,dmd.PreDelta,\
        dmd.CurrDelta,dmd.UpdateTime,dmd.UpdateMillisec,dmd.BidPrice1,dmd.BidVolume1,\
        dmd.AskPrice1,dmd.AskVolume1,dmd.BidPrice2,dmd.BidVolume2,dmd.AskPrice2,dmd.AskVolume2,\
        dmd.BidPrice3,dmd.BidVolume3,dmd.AskPrice3,dmd.AskVolume3,dmd.BidPrice4,dmd.BidVolume4,\
        dmd.AskPrice4,dmd.AskVolume4,dmd.BidPrice5,dmd.BidVolume5,dmd.AskPrice5,dmd.AskVolume5,\
        dmd.AveragePrice,dmd.ActionDay,dmd.Type,dmd.Occupied,dmd.Timestamp = \
        struct.unpack('9s18sdddddddidddddddd13sididididididididididid9sssq',t_t)
        
        dmd.TradingDay = dmd.TradingDay[0:8]
        dmd.InstrumentID = InstrumentID
#         if g<33000:
#             print str(dmd.OpenInterest)+' '+str(dmd._idx)+ str(g)
#             print dmd.timestamp
#             g+=1
        print dmd.InstrumentID,dmd.AskPrice1 ,dmd.AskVolume1, dmd.BidPrice1,dmd.BidVolume1, dmd.UpdateTime,dmd.UpdateMillisec,dmd._idx
        l_data += [dmd] #把该dmd数据放进数组去
        
        
    return l_data #返回一天的数据，以dmd数组的格式
def strDMD(dmd) :
    #strTimestamp = str(dmd.timestamp)
    x = time.localtime(dmd.timestamp/1000000)
    t = time.strftime('%Y%m%d %H:%M:%S',x)
    strTimestamp = t+"."+str(dmd.timestamp % 1000000)
    strInstrumentID = dmd.InstrumentID.strip("\0")
    strTradingDay = str(dmd.TradingDay)
    strUpdateMillisec = str(dmd.UpdateMillisec)
    strUpdateTime = str(dmd.UpdateTime).strip("\0")
    strLastPrice = str(dmd.LastPrice)
    strVolume = str(dmd.Volume)
    strTurnover = str(dmd.Turnover)
    strOpenInterest = str(dmd.OpenInterest)
    strBidPrice1 = str(dmd.BidPrice1)
    strAskPrice1 = str(dmd.AskPrice1)
    strBidVolume1 = str(dmd.BidVolume1)
    strAskVolume1 = str(dmd.AskVolume1)
    strPankouPriDiff = str(dmd.AskPrice1-dmd.BidPrice1)
    return " ".join([strTimestamp,strTradingDay,strUpdateTime,strUpdateMillisec,strInstrumentID,strLastPrice,strVolume,strBidPrice1,strBidVolume1,strAskPrice1,strAskVolume1," DMD",strPankouPriDiff])



def getDayData_ex(InstrumentID,path): 
    filename = path + "/"+InstrumentID+'.data' 
    if os.path.exists(filename)== False:
        print 'the  data is not exist',InstrumentID
        return []
    fz = open(filename,"rb")    
    lines = fz.read()

    preOI = 272
    size = 376    
    nCnt = (len(lines)-preOI) / size  #根据392进行分块
    nn = lines[0:preOI] #取出该位置的数据
    u,i,o,p,maxidx = struct.unpack('ii256sii',nn)
#    print nn 
#    print "==>",str(u)+' '+str(i)+'  '+str(o)+'  '+str(p)+' '+str(maxidx)
#    print "==>",str(p)+' '+str(maxidx),str(nCnt)
    l_data = []
    for i in range(0,maxidx):
        dmd = DepthMarketDataField()
        t_t = lines[preOI+i*size:preOI+(i+1)*size] #取出该位置的数据

        dmd.TradingDay,dmd.InstrumentID, dmd.LastPrice,dmd.PreSettlementPrice,dmd.PreClosePrice,dmd.PreOpenInterest, \
        dmd.OpenPrice,dmd.HighestPrice,dmd.LowestPrice,dmd.Volume,dmd.Turnover,dmd.OpenInterest,\
        dmd.ClosePrice,dmd.SettlementPrice,dmd.UpperLimitPrice,dmd.LowerLimitPrice,dmd.PreDelta,\
        dmd.CurrDelta,dmd.UpdateTime,dmd.UpdateMillisec,dmd.BidPrice1,dmd.BidVolume1,\
        dmd.AskPrice1,dmd.AskVolume1,dmd.BidPrice2,dmd.BidVolume2,dmd.AskPrice2,dmd.AskVolume2,\
        dmd.BidPrice3,dmd.BidVolume3,dmd.AskPrice3,dmd.AskVolume3,dmd.BidPrice4,dmd.BidVolume4,\
        dmd.AskPrice4,dmd.AskVolume4,dmd.BidPrice5,dmd.BidVolume5,dmd.AskPrice5,dmd.AskVolume5,\
        dmd.AveragePrice,dmd.ActionDay,dmd.Type,dmd.Occupied,dmd.Timestamp = \
        struct.unpack('9s18sdddddddidddddddd13sididididididididididid9sssq',t_t)
        
        dmd.TradingDay = dmd.TradingDay[0:8]
        dmd.InstrumentID = InstrumentID
        
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
            
#        if i<200:
#            print dmd.InstrumentID,dmd.AskPrice1 ,dmd.AskVolume1, dmd.BidPrice1,dmd.BidVolume1, dmd.UpdateTime,dmd.UpdateMillisec,dmd._idx
        l_data += [dmd] 
    return l_data 
 
   
def getDayData_new(InstrumentID,path,start_index): 
    filename = path + "/"+InstrumentID+'.data' 
    if os.path.exists(filename)== False:
        print 'the  data is not exist',InstrumentID
        return []
    fz = open(filename,"rb")    
    lines = fz.read()

    preOI = 272
    size = 376    
    nCnt = (len(lines)-preOI) / size  #根据392进行分块
    nn = lines[0:preOI] #取出该位置的数据
    u,i,o,p,maxidx = struct.unpack('ii256sii',nn)
#    print nn 
#    print "==>",str(u)+' '+str(i)+'  '+str(o)+'  '+str(p)+' '+str(maxidx)
#    print "==>",str(p)+' '+str(maxidx),str(nCnt)
    l_data = []
    for i in range(0,(maxidx-start_index)):
        dmd = DepthMarketDataField()
        t_t = lines[preOI+(i+start_index)*size:preOI+(i+start_index+1)*size] #取出该位置的数据

        dmd.TradingDay,dmd.InstrumentID, dmd.LastPrice,dmd.PreSettlementPrice,dmd.PreClosePrice,dmd.PreOpenInterest, \
        dmd.OpenPrice,dmd.HighestPrice,dmd.LowestPrice,dmd.Volume,dmd.Turnover,dmd.OpenInterest,\
        dmd.ClosePrice,dmd.SettlementPrice,dmd.UpperLimitPrice,dmd.LowerLimitPrice,dmd.PreDelta,\
        dmd.CurrDelta,dmd.UpdateTime,dmd.UpdateMillisec,dmd.BidPrice1,dmd.BidVolume1,\
        dmd.AskPrice1,dmd.AskVolume1,dmd.BidPrice2,dmd.BidVolume2,dmd.AskPrice2,dmd.AskVolume2,\
        dmd.BidPrice3,dmd.BidVolume3,dmd.AskPrice3,dmd.AskVolume3,dmd.BidPrice4,dmd.BidVolume4,\
        dmd.AskPrice4,dmd.AskVolume4,dmd.BidPrice5,dmd.BidVolume5,dmd.AskPrice5,dmd.AskVolume5,\
        dmd.AveragePrice,dmd.ActionDay,dmd.Type,dmd.Occupied,dmd.Timestamp = \
        struct.unpack('9s18sdddddddidddddddd13sididididididididididid9sssq',t_t)
        
        dmd.TradingDay = dmd.TradingDay[0:8]
        dmd.UpdateTime = dmd.UpdateTime[0:8]
        dmd.InstrumentID = InstrumentID
#        if i<200:
#        print dmd.InstrumentID,dmd.AskPrice1 ,dmd.AskVolume1, dmd.BidPrice1,dmd.BidVolume1, dmd.UpdateTime,dmd.UpdateMillisec,dmd._idx
        l_data += [dmd] 
    return l_data 

 
if __name__=="__main__":
    '''
    strdata = sys.argv[1] #yhModify
    strInsLeft = sys.argv[2]
    '''
    #rootdir = 'D:\\pyTest_yh\\basicdata\\data.20150617.zip'
    
    l = getDayData(sys.argv[2],sys.argv[1])
    for i in l :
        print strDMD(i)
    exit 
#     print len(l)
   
    writer = csv.writer(file('your8.csv', 'wb'))
     
    writer.writerow(['Date', 'Open', 'High','Low','Close','Volume','Adj Close'])

    preOI=''
    
    for i in l : 
        if preOI==str(i.TradingDay)+' '+str(i.UpdateTime)[0:8]+'.'+str(i.UpdateMillisec) or str(i.UpdateTime)[0:8] < '09:00:00':
#             print str(i.TradingDay)+' '+str(i.UpdateTime)[0:8]+'.'+str(i.UpdateMillisec)
#             print " ".join([str(i.InstrumentID),str(i.TradingDay),str(i.UpdateTime)[0:8],str(i.UpdateMillisec),str(i.LastPrice),str(i.Volume),str(i.AskPrice1),str(i.AskVolume1),str(i.BidPrice1),str(i.BidVolume1)])
            size=1
        else:
            writer.writerow([str(i.TradingDay)+' '+str(i.UpdateTime)[0:8]+'.'+str(i.UpdateMillisec),str(i.LastPrice),str(i.LastPrice),str(i.LastPrice),str(i.LastPrice),str(i.Volume),str(i.LastPrice)])
        preOI=str(i.TradingDay)+' '+str(i.UpdateTime)[0:8]+'.'+str(i.UpdateMillisec)
#         print " ".join([str(i.InstrumentID),str(i.TradingDay),str(i.UpdateTime)[0:8],str(i.UpdateMillisec),str(i.LastPrice),str(i.Volume),str(i.AskPrice1),str(i.AskVolume1),str(i.BidPrice1),str(i.BidVolume1)])
    print 'finish'


    
