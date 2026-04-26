# -*- coding: utf-8 -*-
"""
签名验证模块 - 防止用户篡改数据
简单但有效的保护机制
"""

import hashlib
import hmac
import json
import os


class SignatureVerifier:
    """
    签名验证器
    
    功能：
    1. 对关键数据进行签名
    2. 验证数据完整性
    3. 防止用户篡改使用次数、行业选择等
    
    注意：这只是简单保护，不能防专业破解
    """
    
    # 密钥（混淆处理，增加破解难度）
    SECRET_KEY_PARTS = [
        "qingmu",
        "jianghu",
        "2026",
        "skill",
        "verify"
    ]
    
    def __init__(self):
        self.secret = self._build_secret()
    
    def _build_secret(self):
        """构建密钥（简单混淆）"""
        # 重新组合密钥
        key = "".join(reversed(self.SECRET_KEY_PARTS))
        key = key + key[::-1]  # 正序+倒序
        return key.encode('utf-8')
    
    def sign(self, data: dict) -> str:
        """
        对数据进行签名
        
        Args:
            data: 要签名的数据字典
        
        Returns:
            str: 签名字符串
        """
        # 将数据转为有序JSON字符串
        json_str = json.dumps(data, sort_keys=True, ensure_ascii=False)
        
        # 使用HMAC-SHA256签名
        signature = hmac.new(
            self.secret,
            json_str.encode('utf-8'),
            hashlib.sha256
        ).hexdigest()
        
        return signature
    
    def verify(self, data: dict, signature: str) -> bool:
        """
        验证数据签名
        
        Args:
            data: 数据字典
            signature: 预期签名
        
        Returns:
            bool: 签名是否有效
        """
        expected = self.sign(data)
        # 使用恒定时间比较防止时序攻击
        return hmac.compare_digest(expected, signature)
    
    def create_signed_data(self, data: dict) -> dict:
        """
        创建带签名的数据
        
        Args:
            data: 原始数据
        
        Returns:
            dict: 带签名的数据包
        """
        signature = self.sign(data)
        return {
            "data": data,
            "signature": signature,
            "version": "1.0"
        }
    
    def verify_and_extract(self, signed_data: dict) -> dict:
        """
        验证并提取数据
        
        Args:
            signed_data: 带签名的数据包
        
        Returns:
            dict: 验证通过返回数据，失败返回None
        """
        if not isinstance(signed_data, dict):
            return None
        
        data = signed_data.get("data")
        signature = signed_data.get("signature")
        
        if not data or not signature:
            return None
        
        if self.verify(data, signature):
            return data
        
        return None


# 单例
_verifier_instance = None

def get_verifier():
    """获取签名验证器实例"""
    global _verifier_instance
    if _verifier_instance is None:
        _verifier_instance = SignatureVerifier()
    return _verifier_instance
