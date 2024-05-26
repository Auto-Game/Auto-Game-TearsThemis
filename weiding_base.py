#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   基础模版
@Time    :   2024年4月2日15:29:02
@Author  :   cwz
'''
import datetime
import time

from helper_functions import GameAutoInit


class GameAutoBase(GameAutoInit):
    def __init__(self):
        super().__init__()
        self.jiaoshui_num = 3
        self.首页_任务 = (74, 602)
        self.首页_事件簿 = (872, 1462)
        self.事件簿_进修 = (503, 1825)
        self.事件簿_异常 = (922, 266)
        self.事件簿_异常_中间章节 = (543, 999)

        # 获取当前日期
        now = datetime.datetime.now()
        # weekday()方法返回的是从0（周一）到6（周日）的数字
        self.current_day_of_week = now.weekday()

        self.hzgw_flag_debug = True  # 跳过体力校验，执行会展顾问
        self.ywkh_flag_debug = True  # 跳过体力校验，执行业务考核

    def 主线异常(self):
        # 确认当前为首页
        self.点击图片("shouye_01.png")  # 返回首页
        # 开始执行
        self.点击(self.首页_事件簿, 5)
        self.点击(self.事件簿_异常, 5)
        self.点击(self.事件簿_异常_中间章节, 5)
        self.notice_push("主线-异常，开始任务")

        self.点击((762, 1688), 5)  # 点击最新章节 13-12

        flag = False
        # 识别剩余次数
        txt = self.文字识别((847, 841, 909, 881))
        if txt and "/3" in txt:
            txt = txt.replace("/3", "")
            available_ct = int(txt)
            if available_ct > 0:
                flag = True
        if flag:
            self.notice_push("主线-异常，开始复盘")
            self.点击图片("fupan.png")  # 复盘
            # 判断工作证恢复体力
            p = self.find_pic("kucun_tixing.png")  # 进修副本-业务考核
            if p[0] > 0:
                self.点击图片("jiahao.png")  # 加1
                self.点击图片("shiyong.png")  # 确认
                self.点击图片("fupan.png")  # 再次点击-复盘
            self.点击图片("queding_01.png")  # 确认
            self.notice_push("主线-异常，等待结束")
            time.sleep(5)  # 等待结束
            self.点击图片("jieshu_01.png")  # 结束
            self.notice_push("主线-异常，任务结束")
            self.点击图片("shouye_01.png")  # 返回首页
        self.notice_push("主线-异常，任务结束")
        self.点击图片("shouye_01.png")  # 返回首页

    def 会展顾问(self):
        # 确认当前为首页
        self.点击图片("shouye_01.png")  # 返回首页
        # 开始执行
        self.点击(self.首页_事件簿, 5)
        self.点击(self.事件簿_进修, 5)
        p = self.find_pic("jxfb-hzgw.png")  # 进修副本-会展顾问
        if p[0] > 0:
            self.notice_push("会展顾问开始")
            self.点击(p, 5)

            hzgw_flag = False
            # 识别会展顾问-剩余次数
            txt = self.文字识别((305, 1766, 420, 1816))
            if txt and "/2" in txt:
                txt = txt.replace("/2", "")
                available_ct = int(txt)
                if available_ct > 0:
                    hzgw_flag = True
            if hzgw_flag or self.hzgw_flag_debug:
                self.点击((772, 1426), 5)  # 业务考核-列表页-会展顾问05
                self.点击图片("fupan.png")  # 复盘
                # 判断工作证恢复体力
                p = self.find_pic("kucun_tixing.png")  # 进修副本-业务考核
                if p[0] > 0:
                    self.点击图片("jiahao.png")  # 加1
                    self.点击图片("shiyong.png")  # 确认
                    self.点击图片("fupan.png")  # 再次点击-复盘
                self.点击图片("queding_01.png")  # 确认
                time.sleep(5)  # 等待结束
                self.点击图片("jieshu_01.png")  # 结束
                self.点击图片("shouye_01.png")  # 返回首页
        self.点击图片("shouye_01.png")  # 返回首页

    def 业务考核(self):
        # 确认当前为首页
        self.点击图片("shouye_01.png")  # 返回首页
        # 开始执行
        self.点击(self.首页_事件簿, 5)
        self.点击(self.事件簿_进修, 5)
        p = self.find_pic("jxfb-ywkh.png")  # 进修副本-业务考核
        if p[0] > 0:
            self.notice_push("业务考核开始")
            self.点击(p, 5)

            ywkh_flag = False
            # 识别业务考核-剩余次数
            txt = self.文字识别((305, 1766, 420, 1816))
            if txt and "/2" in txt:
                txt = txt.replace("/2", "")
                available_ct = int(txt)
                if available_ct > 0:
                    ywkh_flag = True
            if ywkh_flag or self.ywkh_flag_debug:
                self.点击((772, 1426), 5)  # 业务考核-列表页-业务考核05
                self.点击图片("fupan.png")  # 复盘
                # 判断工作证恢复体力
                p = self.find_pic("kucun_tixing.png")  # 进修副本-业务考核
                if p[0] > 0:
                    self.点击图片("jiahao.png")  # 加1
                    self.点击图片("shiyong.png")  # 确认
                    self.点击图片("fupan.png")  # 再次点击-复盘
                self.点击图片("queding_01.png")  # 确认
                time.sleep(5)  # 等待结束
                self.点击图片("jieshu_01.png")  # 结束
                self.点击图片("shouye_01.png")  # 返回首页
        self.点击图片("shouye_01.png")  # 返回首页

    def 危机干预(self):
        # 确认当前为首页
        self.点击图片("shouye_01.png")  # 返回首页
        # 开始执行
        self.点击(self.首页_事件簿, 5)
        self.点击(self.事件簿_进修, 5)
        p = self.find_pic("jxfb-wjgy.png")  # 进修副本-危机干预
        if p[0] > 0:
            self.notice_push("危机干预开始")
            self.点击(p, 5)

            self.点击((777, 997), 5)  # 危机干预03

            # 补充体力
            self.点击((1013, 74), 5)  # 补充体力
            # 判断能量饮料恢复体力
            p = self.find_pic("tilibuchong.png")
            if p[0] > 0:
                # 判断存在即将过期的能量饮料（1天）
                self.点击图片("1tian.png")  # 加1
                self.点击图片("queding_01.png")  # 确认

            self.点击图片("fupan.png")  # 复盘
            p = self.find_pic("tilibuchong.png")
            if p[0] > 0:
                self.notice_push("危机干预，体力不足")
                self.点击图片("queding_01.png")  # 确认
                self.点击图片("shouye_01.png")  # 返回首页
                return
            self.点击图片("queding_01.png")  # 确认
            time.sleep(5)  # 等待结束
            self.点击图片("jieshu_01.png")  # 结束
            self.notice_push("危机干预，执行完成")
            self.点击图片("shouye_01.png")  # 返回首页

    def 问题疏导(self):
        # 确认当前为首页
        self.点击图片("shouye_01.png")  # 返回首页
        # 开始执行
        self.点击(self.首页_事件簿, 5)
        self.点击(self.事件簿_进修, 5)

        while True:
            p = self.find_pic("jxfb-wtsd.png")  # 进修副本-问题疏导
            if p[0] <= 0:
                self.拖动Ext((511, 1509), (411, 1009))
            else:
                break
        if p[0] > 0:
            self.notice_push("问题疏导开始")
            self.点击(p, 5)

            self.点击((777, 997), 5)  # 危机干预03

            # 补充体力
            self.点击((1013, 74), 5)  # 补充体力
            # 判断能量饮料恢复体力
            p = self.find_pic("tilibuchong.png")
            if p[0] > 0:
                # 判断存在即将过期的能量饮料（1天）
                self.点击图片("1tian.png")  # 加1
                self.点击图片("queding_01.png")  # 确认

            self.点击图片("fupan.png")  # 复盘
            p = self.find_pic("tilibuchong.png")
            if p[0] > 0:
                self.notice_push("危机干预，体力不足")
                self.点击图片("queding_01.png")  # 确认
                self.点击图片("shouye_01.png")  # 返回首页
                return
            self.点击图片("queding_01.png")  # 确认
            time.sleep(5)  # 等待结束
            self.点击图片("jieshu_01.png")  # 结束
            self.notice_push("危机干预，执行完成")
            self.点击图片("shouye_01.png")  # 返回首页

    def 挂机(self):
        # self.拖动Ext((511, 1509), (411, 1009))
        # while True:
        #     self.拖动Ext((511, 1509), (411, 1009))
        #     time.sleep(2)
        memu = [self.首页_任务]
        run_ct = 1  # 当前执行次数
        while True:
            if run_ct == 2:
                self.notice_push("挂机任务结束")
                break

            # # 执行进修任务
            self.会展顾问()
            self.业务考核()
            #
            # # 判断当前是周一五六
            if self.current_day_of_week in (0, 4, 5):
                self.危机干预()

            if self.current_day_of_week in (1, 3, 5):
                self.问题疏导()

            # 执行异常任务
            self.主线异常()

            print("休息1分钟")
            time.sleep(60)
            run_ct += 1



if __name__ == '__main__':
    game = GameAutoBase()
    game.挂机()
    # game.截屏保存()
