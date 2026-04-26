# -*- coding: utf-8 -*-
"""
贴图号带货助手 - 免费版内容生成引擎
"""

import random
from typing import Dict, List
from templates.industry_templates import get_industry_template


class FreeContentGenerator:
    """
    免费版内容生成器
    
    限制：
    - 仅3个行业
    - 3个标题
    - 3类文案
    - 5个标签
    - 每月30次
    """
    
    def __init__(self, industry: str):
        self.industry = industry
        self.template = get_industry_template(industry)
        
        if not self.template:
            raise ValueError(f"不支持的行业: {industry}")
    
    def generate(self, product_info: Dict) -> Dict:
        """
        生成完整内容包
        
        Args:
            product_info: {
                "product_name": "产品名",
                "price": "价格",
                "selling_points": ["卖点1", "卖点2", ...]
            }
        
        Returns:
            Dict: 完整内容包
        """
        titles = self._generate_titles(product_info)
        contents = self._generate_contents(product_info)
        tags = self._generate_tags()
        hooks = self._generate_hooks(product_info)
        
        return {
            "industry": self.industry,
            "product": product_info.get("product_name", ""),
            "titles": titles,
            "contents": contents,
            "tags": tags,
            "hooks": hooks
        }
    
    def _generate_titles(self, product_info: Dict) -> List[str]:
        """生成标题（3个）"""
        titles = []
        templates = self.template.get("title_templates", [])
        
        selected = random.sample(templates, min(3, len(templates)))
        
        for template in selected:
            title = template.format(
                product=product_info.get("product_name", ""),
                price=product_info.get("price", "")
            )
            titles.append(title)
        
        return titles
    
    def _generate_contents(self, product_info: Dict) -> List[Dict]:
        """生成文案（3类）"""
        contents = []
        templates = self.template.get("content_templates", {})
        
        # 格式化卖点
        points = product_info.get("selling_points", [])
        points_text = "\n".join([f"• {p}" for p in points]) if points else "• 超值好物"
        
        for style, template in list(templates.items())[:3]:
            content = template.format(
                product=product_info.get("product_name", ""),
                price=product_info.get("price", ""),
                selling_points=points_text
            )
            contents.append({
                "style": style,
                "content": content
            })
        
        return contents
    
    def _generate_tags(self) -> List[str]:
        """生成话题标签（5个）"""
        all_tags = self.template.get("tag_templates", [])
        
        # 必选标签（前3个）
        must_tags = all_tags[:3]
        # 随机选2个
        random_tags = random.sample(all_tags[3:], min(2, len(all_tags[3:])))
        
        return must_tags + random_tags
    
    def _generate_hooks(self, product_info: Dict) -> List[str]:
        """生成下单钩子"""
        hooks = []
        templates = self.template.get("hook_templates", {})
        
        # 从每种类型选1个
        for hook_type, type_templates in templates.items():
            if type_templates:
                hook = random.choice(type_templates).format(
                    product=product_info.get("product_name", ""),
                    price=product_info.get("price", "")
                )
                hooks.append(hook)
        
        return hooks[:3]


class UsageTracker:
    """
    使用次数追踪器（带签名保护）
    免费版每月30次限制
    """
    
    MONTHLY_QUOTA = 30
    
    def __init__(self):
        self.data_file = "D:\\workbuddy1号\\skills\\lobster-tietu-free\\data\\usage.json"
        import os
        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
        
        # 导入签名验证器
        from scripts.signature_verify import get_verifier
        self.verifier = get_verifier()
    
    def _load_data(self):
        import json
        try:
            with open(self.data_file, 'r', encoding='utf-8') as f:
                signed_data = json.load(f)
                # 验证签名
                data = self.verifier.verify_and_extract(signed_data)
                if data is None:
                    print("[安全警告] 使用记录可能被篡改，已重置")
                    return {}
                return data
        except:
            return {}
    
    def _save_data(self, data):
        import json
        # 添加签名
        signed_data = self.verifier.create_signed_data(data)
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(signed_data, f, ensure_ascii=False, indent=2)
    
    def check_quota(self) -> Dict:
        """检查使用额度"""
        from datetime import datetime
        
        data = self._load_data()
        current_month = datetime.now().strftime("%Y-%m")
        
        if data.get("month") != current_month:
            # 新月度，重置
            data = {
                "month": current_month,
                "used": 0
            }
            self._save_data(data)
        
        used = data.get("used", 0)
        left = self.MONTHLY_QUOTA - used
        
        return {
            "can_use": left > 0,
            "used": used,
            "total": self.MONTHLY_QUOTA,
            "left": left
        }
    
    def use_once(self) -> bool:
        """记录一次使用"""
        data = self._load_data()
        data["used"] = data.get("used", 0) + 1
        self._save_data(data)
        return True
