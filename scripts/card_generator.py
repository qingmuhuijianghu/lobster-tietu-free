# -*- coding: utf-8 -*-
"""
贴图号带货助手 - 免费版图片生成器
生成4张1080x1440px贴图号卡片
"""

from PIL import Image, ImageDraw, ImageFont
import os


class FreeCardGenerator:
    """
    免费版卡片生成器
    生成4张基础卡片
    """
    
    # 贴图号标准尺寸
    CARD_WIDTH = 1080
    CARD_HEIGHT = 1440
    
    def __init__(self, industry: str):
        self.industry = industry
    
    def generate_cards(self, content_package: dict) -> list:
        """
        生成4张贴图号卡片
        
        Args:
            content_package: 内容包
        
        Returns:
            list: 图片路径列表
        """
        cards = []
        
        # 标题卡
        cards.append(self._create_title_card(content_package))
        
        # 卖点卡
        cards.append(self._create_points_card(content_package))
        
        # 文案卡1
        if content_package.get("contents"):
            cards.append(self._create_content_card(content_package["contents"][0]))
        
        # 标签+钩子卡
        cards.append(self._create_tags_card(content_package))
        
        return [c for c in cards if c]
    
    def _create_title_card(self, content: dict) -> str:
        """创建标题卡片"""
        img = Image.new('RGB', (self.CARD_WIDTH, self.CARD_HEIGHT), '#FFF8F5')
        draw = ImageDraw.Draw(img)
        
        # 尝试加载字体
        try:
            font_title = ImageFont.truetype("msyh.ttc", 60)
            font_sub = ImageFont.truetype("msyh.ttc", 36)
        except:
            font_title = ImageFont.load_default()
            font_sub = ImageFont.load_default()
        
        # 绘制标题
        title = content.get("titles", ["好物推荐"])[0] if content.get("titles") else "好物推荐"
        
        # 简单居中绘制
        draw.text((100, 400), title, fill='#1A1A1A', font=font_title)
        draw.text((100, 550), f"行业: {self.industry}", fill='#666666', font=font_sub)
        draw.text((100, 650), f"产品: {content.get('product', '')}", fill='#666666', font=font_sub)
        
        # 添加装饰线
        draw.rectangle([80, 350, 1000, 355], fill='#FF6B35')
        
        # 保存
        output_dir = "D:\\workbuddy1号\\skills\\lobster-tietu-free\\output"
        os.makedirs(output_dir, exist_ok=True)
        
        filename = f"{output_dir}\\{self.industry}_标题卡.png"
        img.save(filename, 'PNG')
        
        return filename
    
    def _create_points_card(self, content: dict) -> str:
        """创建卖点卡片"""
        img = Image.new('RGB', (self.CARD_WIDTH, self.CARD_HEIGHT), '#FFFFFF')
        draw = ImageDraw.Draw(img)
        
        try:
            font_title = ImageFont.truetype("msyh.ttc", 48)
            font_point = ImageFont.truetype("msyh.ttc", 32)
        except:
            font_title = ImageFont.load_default()
            font_point = ImageFont.load_default()
        
        # 标题
        draw.text((80, 150), "核心卖点", fill='#1A1A1A', font=font_title)
        draw.rectangle([80, 220, 200, 225], fill='#FF6B35')
        
        # 卖点列表
        y = 300
        points = content.get("selling_points", ["超值好物"])
        for i, point in enumerate(points[:4], 1):
            draw.text((80, y), f"{i}. {point}", fill='#333333', font=font_point)
            y += 80
        
        # 保存
        output_dir = "D:\\workbuddy1号\\skills\\lobster-tietu-free\\output"
        filename = f"{output_dir}\\{self.industry}_卖点卡.png"
        img.save(filename, 'PNG')
        
        return filename
    
    def _create_content_card(self, content: dict) -> str:
        """创建文案卡片"""
        img = Image.new('RGB', (self.CARD_WIDTH, self.CARD_HEIGHT), '#FFF8F5')
        draw = ImageDraw.Draw(img)
        
        try:
            font_style = ImageFont.truetype("msyh.ttc", 36)
            font_content = ImageFont.truetype("msyh.ttc", 28)
        except:
            font_style = ImageFont.load_default()
            font_content = ImageFont.load_default()
        
        # 风格标签
        style = content.get("style", "种草")
        draw.rectangle([80, 100, 300, 160], fill='#FF6B35')
        draw.text((110, 115), style, fill='#FFFFFF', font=font_style)
        
        # 文案内容（简化展示）
        content_text = content.get("content", "")[:200] + "..."
        
        # 分行绘制
        y = 220
        lines = content_text.split('\n')
        for line in lines[:10]:
            draw.text((80, y), line, fill='#333333', font=font_content)
            y += 50
        
        # 保存
        output_dir = "D:\\workbuddy1号\\skills\\lobster-tietu-free\\output"
        filename = f"{output_dir}\\{self.industry}_文案卡.png"
        img.save(filename, 'PNG')
        
        return filename
    
    def _create_tags_card(self, content: dict) -> str:
        """创建标签卡片"""
        img = Image.new('RGB', (self.CARD_WIDTH, self.CARD_HEIGHT), '#FFFFFF')
        draw = ImageDraw.Draw(img)
        
        try:
            font_title = ImageFont.truetype("msyh.ttc", 40)
            font_tag = ImageFont.truetype("msyh.ttc", 28)
            font_hook = ImageFont.truetype("msyh.ttc", 32)
        except:
            font_title = ImageFont.load_default()
            font_tag = ImageFont.load_default()
            font_hook = ImageFont.load_default()
        
        # 标签区域
        draw.text((80, 150), "话题标签", fill='#1A1A1A', font=font_title)
        
        tags = content.get("tags", [])[:5]
        y = 250
        for tag in tags:
            draw.rectangle([80, y, 300, y + 50], outline='#FF6B35', width=2)
            draw.text((100, y + 10), f"#{tag}", fill='#FF6B35', font=font_tag)
            y += 70
        
        # 钩子区域
        draw.text((80, 650), "下单引导", fill='#1A1A1A', font=font_title)
        hooks = content.get("hooks", ["左下角链接购买"])[:2]
        y = 750
        for hook in hooks:
            draw.text((80, y), f"• {hook}", fill='#666666', font=font_hook)
            y += 60
        
        # 保存
        output_dir = "D:\\workbuddy1号\\skills\\lobster-tietu-free\\output"
        filename = f"{output_dir}\\{self.industry}_标签卡.png"
        img.save(filename, 'PNG')
        
        return filename
