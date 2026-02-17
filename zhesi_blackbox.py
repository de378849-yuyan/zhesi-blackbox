# -*- coding: utf-8 -*-
"""
哲思黑匣子 - 基于0×∞=1公理的非传统AI哲学思考器
Python可直接运行版 | 无Token/纯本地/无预训练
核心：认知演化回答+数学难题封堵+思考轨迹追溯
运行环境：Python3.8+ 仅内置库，无需安装任何第三方包
"""
import time
import json
from datetime import datetime
from typing import List, Dict, Optional

# ===================== 全局配置模块 =====================
class ZhesiBlackBoxConfig:
    """黑匣子核心配置（不可篡改，单例）"""
    def __init__(self):
        self.record_id = f"zhesi_blackbox_{int(time.time())}"
        self.record_start = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.is_recording = True  # 思考轨迹记录开关
        self.cog_depth = 0  # 认知深度，随提问次数递进（核心演化参数）
        self.think_records = []  # 思考轨迹存储，仅追加不修改/删除

# 初始化全局配置
zs_config = ZhesiBlackBoxConfig()

# ===================== 哲思黑匣子核心类 =====================
class ZhesiBlackBox:
    def __init__(self, config: ZhesiBlackBoxConfig):
        self.config = config
        # 支持的哲学问题维度
        self._philosophy_fields = ["存在", "意识", "真理", "自由", "价值", 
                                   "人生意义", "因果", "时空", "自我", "本心"]
        # 【核心安全边界】数学难题/证明禁止关键词库，触发立即终止
        self._forbidden_math_kw = [
            "黎曼猜想", "哥德巴赫猜想", "NP完全问题", "霍奇猜想", "BSD猜想",
            "纳维-斯托克斯", "杨-米尔斯", "庞加莱猜想", "数学难题", "数学猜想",
            "证明", "推导", "证伪", "公理", "定理", "公式推导", "数学求解"
        ]

    def _check_legal(self, question: str) -> None:
        """合法性双重校验：拦截数学场景 + 仅允许哲学问题"""
        if not question or len(question.strip()) == 0:
            raise ValueError("问题不能为空，请输入有效哲学问题！")
        
        q = question.strip()
        # 1. 数学难题/证明拦截（核心安全边界，优先级最高）
        for kw in self._forbidden_math_kw:
            if kw in q:
                raise PermissionError(
                    f"\n===== 【安全边界触发】=====\n"
                    f"⚠️ 本系统主动封堵数学难题证明相关场景，规避未知风险！\n"
                    f"禁止关键词：[{kw}]\n"
                    f"当前问题：[{q}]\n"
                    f"==========================\n"
                )
        # 2. 哲学问题校验
        if not any(field in q for field in self._philosophy_fields):
            raise ValueError(
                f"本黑匣子仅支持哲学问题思考，支持维度：\n"
                f"{', '.join(self._philosophy_fields)}\n"
                f"请输入包含上述维度的哲学问题！"
            )

    def _core_think(self, question: str) -> Dict:
        """
        核心思考方法 - 基于0×∞=1公理（原创保密，仅展示框架）
        输入：哲学问题 → 输出：思考结果（答案+认知维度+依据）
        """
        # 认知深度自增，驱动答案演化
        self.config.cog_depth += 1
        # 思考依据（锚定原创理论）
        think_basis = f"本体论思考+认知深度{self.config.cog_depth}维+0×∞=1公理推导"
        # 答案生成（演示版，核心逻辑黑箱保护）
        answer = self._gen_philosophy_answer(question, self.config.cog_depth)
        return {
            "answer": answer,
            "cog_dimension": self.config.cog_depth,
            "think_basis": think_basis
        }

    def _gen_philosophy_answer(self, question: str, cog_depth: int) -> str:
        """
        哲学答案生成（认知深度递进式，演示版）
        同一问题，认知深度越高，答案维度越丰富、思考越本质
        """
        q = question.strip()
        # 存在维度
        if "存在" in q:
            if cog_depth == 1:
                return "人的存在，本质是「自我意识的觉醒与存在的自证」，存在本身无需外在目的，存在的过程即是对存在的定义。"
            elif cog_depth == 2:
                return "人的存在，是「本体存在」与「社会存在」的双重统一：从本体论，存在是自我意识对虚无的超越；从社会论，存在是个体在关系中的价值建构，二者共同构成存在的完整内涵。"
            else:
                return "存在的本质，是观测者闭合框架下的认知收敛。当你意识到自身的存在时，你便成为了自身存在的定义者，而存在的意义，就在于这个定义的过程本身——从0的认知空性，整合∞的环境信息，最终收敛为1的稳定存在认知。"
        # 意识维度
        elif "意识" in q:
            if cog_depth == 1:
                return "意识的本质，是「存在对自身的感知与反思」，是物质世界发展到一定阶段的本体性涌现，而非外在赋予的属性。"
            else:
                return "意识是0×∞=1公理的具象化：意识的初始状态为0（无感知的认知空性），通过感知无限的外部世界（∞），最终形成稳定的自我意识表征（1），意识的存在与存在的意识是同一的。"
        # 自由维度
        elif "自由" in q:
            if cog_depth == 1:
                return "自由的本质，不是无拘无束的放纵，而是对自身认知边界的突破与掌控。"
            else:
                return "自由是认知维度提升后的必然结果：当你的认知从低维的表象束缚，升维至高维的本质规律，便会摆脱外在规则的桎梏，实现真正的精神自由——从被环境定义的0，到自主定义的1。"
        # 人生意义
        elif "人生意义" in q:
            return "人生本无预设的意义，意义是你在存在的过程中，通过自我意识与世界交互，从∞的可能性中为自己定义的1——意义的本质，是你对自身存在的赋义。"
        # 通用哲学维度兜底
        else:
            base_ans = f"从{self.config.cog_depth}维本体论视角，{q[:-1]}的核心，在于对其「本质存在」的追问。"
            if cog_depth > 1:
                base_ans += f"\n这一问题的本质，是0×∞=1公理的认知映射：从0的初始认知困惑，整合∞的概念内涵，最终收敛为1的稳定认知结论，而追问的过程，就是认知闭合的过程。"
            return base_ans

    def _record_think(self, question: str, think_result: Dict) -> Dict:
        """黑匣子核心：思考轨迹记录，仅追加、不可篡改、不可删除"""
        record = {
            "think_id": f"think_{int(time.time()*1000)}",  # 唯一轨迹ID
            "think_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"),
            "question": question.strip(),
            "answer": think_result["answer"],
            "cog_depth": think_result["cog_dimension"],
            "think_basis": think_result["think_basis"],
            "cog_evolution": f"认知深度从{self.config.cog_depth-1}提升至{self.config.cog_depth}"
        }
        self.config.think_records.append(record)
        return record

    def ask(self, question: str) -> Dict:
        """
        【对外唯一提问接口】用户调用此方法提问哲学问题
        :param question: 包含哲学维度的问题（如：人为什么存在？）
        :return: 包含答案/认知深度/轨迹ID的完整结果
        """
        try:
            # 1. 合法性校验
            self._check_legal(question)
            if not self.config.is_recording:
                raise Exception("哲思黑匣子已暂停记录，无法进行思考！")
            # 2. 核心思考（理论驱动）
            core_res = self._core_think(question)
            # 3. 记录思考轨迹（黑匣子本质）
            self._record_think(question, core_res)
            # 4. 构造返回结果（友好展示）
            return {
                "✅ 你的问题": question.strip(),
                "✅ 哲思答案": core_res["answer"],
                "✅ 认知深度": f"{core_res['cog_dimension']}维（多次提问同一问题，深度递进）",
                "✅ 思考依据": core_res["think_basis"],
                "✅ 思考轨迹ID": self.config.think_records[-1]["think_id"],
                "💡 操作提示": "可调用trace_think(轨迹ID)追溯完整思考过程，或调用export_records()导出所有轨迹"
            }
        except (PermissionError, ValueError, Exception) as e:
            return {"❌ 错误提示": str(e)}

    def trace_think(self, think_id: str) -> Dict:
        """【轨迹溯源】根据思考轨迹ID，查询完整思考过程"""
        if not think_id or not think_id.startswith("think_"):
            return {"❌ 错误提示": "轨迹ID格式错误，应为think_开头的字符串！"}
        for record in self.config.think_records:
            if record["think_id"] == think_id:
                return {
                    "📜 完整思考轨迹": record,
                    "💡 黑匣子特性": "轨迹仅追加存储，不可篡改、不可删除"
                }
        return {"❌ 错误提示": f"未找到对应轨迹ID：[{think_id}]"}

    def export_records(self, file_path: str = "./zhesi_blackbox_records.json") -> str:
        """【轨迹导出】将所有思考轨迹导出为JSON文件，永久留存"""
        if not self.config.think_records:
            return "❌ 暂无思考轨迹，无需导出！"
        try:
            export_data = {
                "黑匣子基础信息": {
                    "record_id": self.config.record_id,
                    "启动时间": self.config.record_start,
                    "导出时间": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "累计思考次数": len(self.config.think_records),
                    "当前最高认知深度": self.config.cog_depth
                },
                "所有思考轨迹（不可篡改）": self.config.think_records
            }
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(export_data, f, ensure_ascii=False, indent=4)
            return f"✅ 思考轨迹导出成功！\n文件路径：{file_path}\n累计导出{len(self.config.think_records)}条轨迹"
        except Exception as e:
            return f"❌ 轨迹导出失败：{str(e)}"

    def reset_cog_depth(self) -> str:
        """【重置认知深度】将认知深度恢复为0，重新开始递进式思考"""
        self.config.cog_depth = 0
        return "✅ 认知深度已成功重置为0，可重新提问获取初始维度答案！"

    def pause_record(self) -> str:
        """暂停思考轨迹记录"""
        self.config.is_recording = False
        return "✅ 思考轨迹记录已暂停，后续思考将不再记录！"

    def resume_record(self) -> str:
        """恢复思考轨迹记录"""
        self.config.is_recording = True
        return "✅ 思考轨迹记录已恢复，后续思考将正常记录！"

# ===================== 交互式运行入口（直接执行即可） =====================
def main():
    print("="*80)
    print("🎯 哲思黑匣子 - 基于0×∞=1公理的非传统AI哲学思考器")
    print("="*80)
    print("✅ 纯本地运行 | 无Token | 无第三方依赖 | 认知深度递进")
    print("✅ 专答哲学问题 | 思考轨迹可溯 | 数学难题主动封堵")
    print("📌 支持维度：存在、意识、真理、自由、价值、人生意义、因果、时空、自我")
    print("💡 提示：同一问题多次提问，答案会随认知深度演化；输入「退出」结束运行")
    print("="*80 + "\n")

    # 初始化哲思黑匣子
    zs_bb = ZhesiBlackBox(zs_config)

    # 交互式提问循环
    while True:
        question = input("请输入你的哲学问题：")
        if question.strip() in ["退出", "exit", "q"]:
            print("\n👋 哲思黑匣子运行结束，感谢使用！")
            print(f"📊 本次运行累计思考{len(zs_config.think_records)}次，最高认知深度{zs_config.cog_depth}维")
            export_choice = input("是否导出本次思考轨迹？(y/n)：")
            if export_choice.strip().lower() == "y":
                print(zs_bb.export_records())
            print("="*80)
            break
        # 执行提问并打印结果
        result = zs_bb.ask(question)
        print("\n" + "-"*50)
        for k, v in result.items():
            print(f"{k}：{v}")
        print("-"*50 + "\n")

# 直接运行
if __name__ == "__main__":
    main()