#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: nl8590687
用于测试整个一套语音识别系统的程序
语音模型 + 语言模型
"""
import platform as plat

from ASRT.SpeechModel251 import ModelSpeech
from ASRT.LanguageModel import ModelLanguage


ms = ModelSpeech("dataset")

ms.LoadModel('./ASRT/model_speech' + '/' + 'speech_model251_e_0_step_12000.model')
ml = ModelLanguage('./ASRT/model_language')
ml.LoadModel()

def recognize(data):
	import os
	with open("tmp.flac","wb") as f:
		f.write(data)
	os.system('ffmpeg -y -i tmp.flac tmp.wav')




	r = ms.RecognizeSpeech_FromFile('tmp.wav')

	print('*[提示] 语音识别结果：\n',r)

	#str_pinyin = ['zhe4','zhen1','shi4','ji2', 'hao3','de5']
	#str_pinyin = ['jin1', 'tian1', 'shi4', 'xing1', 'qi1', 'san1']
	#str_pinyin = ['ni3', 'hao3','a1']
	str_pinyin = r
	#str_pinyin =  ['su1', 'bei3', 'jun1', 'de5', 'yi4','xie1', 'ai4', 'guo2', 'jiang4', 'shi4', 'ma3', 'zhan4', 'shan1', 'ming2', 'yi1', 'dong4', 'ta1', 'ju4', 'su1', 'bi3', 'ai4', 'dan4', 'tian2','mei2', 'bai3', 'ye3', 'fei1', 'qi3', 'kan4', 'zhan4']
	r = ml.SpeechToText(str_pinyin)
	print('语音转文字结果：\n',r)
	return r
