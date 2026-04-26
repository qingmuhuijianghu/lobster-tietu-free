# -*- coding: utf-8 -*-
"""
龙虾贴图号带货助手 - 免费版
适用于腾讯SkillHub，供学员体验使用
"""

import os
import json
from datetime import datetime

from templates.industry_templates import get_industry_list, get_industry_template
from scripts.content_generator import FreeContentGenerator, UsageTracker
from scripts.card_generator import FreeCardGenerator


def print_header():
    """打印标题"""
    print("\n" + "=" * 60)
    print("[贴图号内容官] 免费版")
    print("   青木会江湖 - 14天新手虾友实战营")
    print("=" * 60)


def check_quota():
    """检查使用额度"""
    tracker = UsageTracker()
    quota = tracker.check_quota()
    
    print(f"\n[额度] 本月使用: {quota['used']}/{quota['total']}次")
    
    if not quota['can_use']:
        print("\n[提示] 本月额度已用完！")
        print("  请下月1日后再使用，或联系青木老贼了解Pro版")
        return False
    
    if quota['left'] <= 5:
        print(f"  还剩{quota['left']}次，注意使用")
    
    return True


def select_industries():
    """选择3个要使用的行业（首次使用）"""
    from templates.industry_templates import get_all_industries_count
    
    all_industries = get_industry_list()
    total = get_all_industries_count()
    
    print("\n[选择行业]")
    print("-" * 50)
    print(f"免费版提供 {total} 个行业模板")
    print("请选择你想要使用的 3 个行业：\n")
    
    for i, industry in enumerate(all_industries, 1):
        print(f"  {i}. {industry}")
    
    print("-" * 50)
    
    selected = []
    while len(selected) < 3:
        prompt = f"\n请选择第 {len(selected)+1} 个行业 [1-{total}]: "
        choice = input(prompt).strip()
        
        if not choice.isdigit():
            print("[错误] 请输入数字")
            continue
        
        idx = int(choice) - 1
        if idx < 0 or idx >= len(all_industries):
            print(f"[错误] 请输入 1-{total} 之间的数字")
            continue
        
        industry = all_industries[idx]
        if industry in selected:
            print(f"[提示] {industry} 已经选过了，请选其他行业")
            continue
        
        selected.append(industry)
        print(f"  ✓ 已选择: {industry}")
    
    # 保存选择
    save_selected_industries(selected)
    
    print(f"\n[完成] 你选择的3个行业是：")
    for i, ind in enumerate(selected, 1):
        print(f"  {i}. {ind}")
    
    return selected


def get_selected_industries():
    """获取已选择的行业（带签名验证）"""
    import json
    import os
    from scripts.signature_verify import get_verifier
    
    data_file = "D:\\workbuddy1号\\skills\\lobster-tietu-free\\data\\selected_industries.json"
    verifier = get_verifier()
    
    if os.path.exists(data_file):
        try:
            with open(data_file, 'r', encoding='utf-8') as f:
                signed_data = json.load(f)
                # 验证签名
                data = verifier.verify_and_extract(signed_data)
                if data is None:
                    print("[安全警告] 行业选择记录可能被篡改，请重新选择")
                    return []
                return data.get("industries", [])
        except:
            pass
    
    return []


def save_selected_industries(industries):
    """保存已选择的行业（带签名）"""
    import json
    import os
    from scripts.signature_verify import get_verifier
    
    data_dir = "D:\\workbuddy1号\\skills\\lobster-tietu-free\\data"
    os.makedirs(data_dir, exist_ok=True)
    
    data_file = os.path.join(data_dir, "selected_industries.json")
    verifier = get_verifier()
    
    # 添加签名
    data = {"industries": industries}
    signed_data = verifier.create_signed_data(data)
    
    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(signed_data, f, ensure_ascii=False, indent=2)


def reset_industries():
    """重置行业选择"""
    import os
    
    data_file = "D:\\workbuddy1号\\skills\\lobster-tietu-free\\data\\selected_industries.json"
    
    if os.path.exists(data_file):
        os.remove(data_file)
        print("\n[成功] 已清空行业选择，可以重新选择")
    else:
        print("\n[提示] 暂无已选行业，直接选择即可")
    
    return select_industries()


def select_industry():
    """选择行业（从已选的3个中选择）"""
    selected = get_selected_industries()
    
    # 首次使用，需要选择3个行业
    if not selected:
        selected = select_industries()
    
    print("\n[选择行业]")
    print("-" * 40)
    print("免费版可使用以下3个行业：\n")
    
    for i, industry in enumerate(selected, 1):
        print(f"  {i}. {industry}")
    
    print("-" * 40)
    print("\n[选项]")
    print("  1-3: 选择行业")
    print("  0: 重新选择行业（更换3个行业）")
    
    while True:
        choice = input("\n请选择 [0-3]: ").strip()
        
        if choice == "0":
            confirm = input("确定要重新选择3个行业吗？之前的选择将清空 (y/n): ").strip().lower()
            if confirm == 'y':
                return reset_industries()
            else:
                print("已取消，继续使用当前3个行业")
                continue
        
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(selected):
                return selected[idx]
        
        print("[错误] 无效选择，请重新输入")


def input_product_info():
    """输入产品信息"""
    print("\n[输入产品信息]")
    print("-" * 40)
    
    product_name = input("产品名称: ").strip()
    price = input("产品价格: ").strip()
    
    print("\n核心卖点（输入3-5个，每个回车，输完输入q结束）:")
    points = []
    while len(points) < 5:
        point = input(f"  卖点{len(points)+1}: ").strip()
        if point.lower() == 'q':
            break
        if point:
            points.append(point)
    
    return {
        "product_name": product_name,
        "price": price,
        "selling_points": points
    }


def generate_content(industry: str, product_info: dict):
    """生成内容"""
    print("\n[生成中] 正在生成内容...")
    
    generator = FreeContentGenerator(industry)
    content = generator.generate(product_info)
    
    # 记录使用
    tracker = UsageTracker()
    tracker.use_once()
    
    return content


def display_results(content: dict):
    """显示结果"""
    print("\n" + "=" * 60)
    print("[生成完成] 贴图号内容包")
    print("=" * 60)
    
    # 标题
    print("\n【爆款标题】（3个）")
    for i, title in enumerate(content.get("titles", []), 1):
        print(f"  {i}. {title}")
    
    # 文案
    print("\n【种草文案】（3类）")
    for item in content.get("contents", []):
        print(f"\n  [{item['style']}]")
        print(f"  {item['content'][:100]}...")
    
    # 标签
    print("\n【话题标签】（5个）")
    tags = content.get("tags", [])
    print("  " + " ".join([f"#{tag}" for tag in tags]))
    
    # 钩子
    print("\n【下单引导】")
    for i, hook in enumerate(content.get("hooks", []), 1):
        print(f"  {i}. {hook}")


def generate_cards(content: dict, industry: str):
    """生成卡片"""
    print("\n[生成中] 正在生成贴图号卡片...")
    
    try:
        generator = FreeCardGenerator(industry)
        cards = generator.generate_cards(content)
        
        if cards:
            print(f"\n[完成] 已生成 {len(cards)} 张卡片")
            print("  保存位置:")
            for card in cards:
                print(f"    - {card}")
        else:
            print("[提示] 卡片生成失败，但文案内容已生成")
    except Exception as e:
        print(f"[提示] 卡片生成失败: {e}")
        print("  但文案内容已生成完成")


def save_results(content: dict):
    """保存结果到文件"""
    output_dir = "D:\\workbuddy1号\\skills\\lobster-tietu-free\\output"
    os.makedirs(output_dir, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{output_dir}\\content_{timestamp}.json"
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(content, f, ensure_ascii=False, indent=2)
    
    print(f"\n[保存] 内容已保存到: {filename}")


def main():
    """主程序"""
    print_header()
    
    # 检查额度
    if not check_quota():
        return
    
    # 选择行业
    industry = select_industry()
    print(f"\n[已选] {industry}")
    
    # 输入产品信息
    product_info = input_product_info()
    
    # 确认生成
    print("\n[确认]")
    print(f"  行业: {industry}")
    print(f"  产品: {product_info['product_name']}")
    print(f"  价格: {product_info['price']}")
    
    confirm = input("\n确认生成？(y/n): ").strip().lower()
    if confirm != 'y':
        print("\n已取消")
        return
    
    # 生成内容
    content = generate_content(industry, product_info)
    
    # 显示结果
    display_results(content)
    
    # 生成卡片
    generate_cards(content, industry)
    
    # 保存结果
    save_results(content)
    
    # 显示剩余额度
    tracker = UsageTracker()
    quota = tracker.check_quota()
    print(f"\n[额度] 本月还剩 {quota['left']} 次")
    
    print("\n" + "=" * 60)
    print("[完成] 内容生成完成！")
    print("=" * 60)
    print("\n使用说明：")
    print("  1. 复制标题和文案到贴图号")
    print("  2. 使用生成的图片作为配图")
    print("  3. 添加话题标签发布")
    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
