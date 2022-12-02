#-*- coding: UTF-8 -*-

import os
import sys
import json
import time

os.system("")
#无语了，颜色转义字符一直失效
#这是玄学的关键，在执行完system()之后，转移序列都会生效，原因未知

logFilePath = ".\\data\\logs\\"
if os.path.exists(logFilePath) == False: os.makedirs(logFilePath)

#日志等级定义
'''
DEBUG：      排查故障时使用的低级别系统信息，通常开发时使用
INFO：       一般的系统信息，并不算问题
WARNING：    描述系统发生小问题的信息，但通常不影响功能
ERROR：      描述系统发生大问题的信息，可能会导致功能不正常
CRITICAL：   描述系统发生严重问题的信息，应用程序有崩溃的风险
'''

#字体
'''

显示方式:
    0   默认
    1   高亮
    2   非高亮
    4   下划线
    5   闪烁(此选项在cmd中会比较明显)
    7   反显
    8   不可见

颜色  前景  背景

黑色   30    40
红色   31    41
绿色   32    42
黄色   33    43
蓝色   34    44
紫色   35    45
天蓝色 36    46
白色   37    47

\033[0m

'''

def logJudge(log=None, pluginName=None):
  if log == None:
    warning("日志内容为空，日志来源：" + pluginName, "logger")
  if pluginName == None:
    warning("日志来源为空，日志内容：" + log, "logger")
  if log != None and pluginName != None:
    return True

def logWrite(logTime=None, logType=None, logSource=None, logText=None):
  logStr = ""
  logData = {}
  if logTime:
    logStr = logStr + "[" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(logTime)) + "]"
    logData["time"] = logTime
  if logType:
    logStr = logStr + "[" + logType + "]"
    logData["type"] = logType
  if logSource:
    logStr = logStr + "[" + logSource + "]"
    logData["source"] = logSource
  if logText:
    logStr = logStr + logText
    logData["text"] = logText
  
  logFilePath = ".\\data\\logs\\" + time.strftime("%Y", time.localtime(logTime)) + "\\" + time.strftime("%Y-%m", time.localtime(logTime)) + "\\" + time.strftime("%Y-%m-%d", time.localtime(logTime))
  if os.path.exists(logFilePath) == False: os.makedirs(logFilePath)
  logFilePath = logFilePath + "\\" + time.strftime("%Y-%m-%d", time.localtime(logTime)) + ".log"

  with open(logFilePath, 'a') as logFile:
    logJson = json.dumps(logData, ensure_ascii=False) + "\r\n"
    logFile.write(logJson)
    #json.dump(logData, logFile, indent=0, ensure_ascii=False)
  
  return logStr


def debug(logText=None, logSource=None):
  logTime = time.time()
  logStr = logWrite(logTime, "debug", logSource, logText)
  print("\033[2m" + logStr + "\033[0m")
  
def info(logText=None, logSource=None):
  logTime = time.time()
  logStr = logWrite(logTime, "info", logSource, logText)
  print("\033[32m" + logStr + "\033[0m")
  
def warning(logText=None, logSource=None):
  logTime = time.time()
  logStr = logWrite(logTime, "warning", logSource, logText)
  print("\033[33m" + logStr + "\033[0m")
  
def error(logText=None, logSource=None):
  logTime = time.time()
  logStr = logWrite(logTime, "error", logSource, logText)
  print("\033[31;47m" + logStr + "\033[0m")
  
def critical(logText=None, logSource=None):
  logTime = time.time()
  logStr = logWrite(logTime, "critical", logSource, logText)
  print("\033[5;31;47m" + logStr + "\033[0m")


if __name__ == "__main__":
  try:
    debug("logger.debug 测试成功！", "test")
  except:
    print("logger.debug 测试失败!")
  try:
    info("logger.info 测试成功！", "test")
  except:
    print("logger.info 测试失败!")
  try:
    warning("logger.warning 测试成功！", "test")
  except:
    print("logger.warning 测试失败!")
  try:
    error("logger.error 测试成功！", "test")
  except:
    print("logger.error 测试失败!")
  try:
    critical("logger.critical 测试成功！", "test")
  except:
    print("logger.critical 测试失败!")
    
  time.sleep(10)