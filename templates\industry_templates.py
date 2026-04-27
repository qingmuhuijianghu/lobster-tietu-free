# -*- coding: utf-8 -*-
"""
贴图号带货助手 - 免费版行业模板
包含所有行业，但限制使用3个
"""

# 免费版包含所有行业模板（但限制只能使用3个）
ALL_INDUSTRIES = {
    "食品零食": {
        "keywords": ["零食", "美食", "好吃", "追剧必备", "办公室", "宿舍", "解馋"],
        "title_templates": [
            "救命！这个{product}也太好吃了吧",
            "挖到宝了！{price}买到一大箱{product}",
            "姐妹们！这个{product}真的绝了"
        ],
        "content_templates": {
            "种草型": """姐妹们！挖到宝了！

这个{product}真的绝了！

{selling_points}

我已经回购3次了，真的好吃到停不下来！
左下角链接，{price}超划算！""",
            "测评型": """【真实测评】{product}

价格：{price}

优点：
{selling_points}

总体：⭐⭐⭐⭐⭐

想试试的姐妹点左下角~""",
            "干货型": """零食怎么选？

今天给大家分享{product}

选购要点：
{selling_points}

闭眼入不踩雷！

价格{price}，左下角链接~"""
        },
        "tag_templates": [
            "零食推荐", "追剧小零食", "办公室零食", "宿舍必备", "解馋神器",
            "好吃到停不下来", "平价零食", "零食测评", "网红零食", "学生党"
        ],
        "color_scheme": {
            "primary": "#FF6B35",
            "secondary": "#FFF8F5",
            "accent": "#FFE4D6"
        }
    },
    
    "服装穿搭": {
        "keywords": ["穿搭", "OOTD", "显瘦", "显高", "百搭", "平价", "学生党"],
        "title_templates": [
            "挖到宝！{price}的{product}太绝了",
            "姐妹们！这件{product}真的显瘦",
            "为什么没人推这个{product}！巨好看"
        ],
        "content_templates": {
            "种草型": """挖到宝了姐妹们！

这件{product}真的绝了！

{selling_points}

穿上瞬间气质up！
{price}超值，左下角链接~""",
            "测评型": """【真实测评】{product}

价格：{price}

上身效果：
{selling_points}

总体：⭐⭐⭐⭐⭐

想入手的点左下角~""",
            "干货型": """穿搭干货 | 怎么选{product}

选购要点：
{selling_points}

这款亲测好穿！

{price}性价比超高，左下角链接~"""
        },
        "tag_templates": [
            "穿搭", "OOTD", "显瘦穿搭", "显高穿搭", "平价穿搭",
            "学生党穿搭", "百搭单品", "穿搭分享", "气质穿搭", "日常穿搭"
        ],
        "color_scheme": {
            "primary": "#4A5568",
            "secondary": "#F7FAFC",
            "accent": "#E2E8F0"
        }
    },
    
    "家居": {
        "keywords": ["家居", "好物", "实用", "收纳", "平价", "提升幸福感"],
        "title_templates": [
            "挖到宝！{price}的{product}太好用了",
            "这个{product}真的绝了！建议人手一个",
            "为什么没人推这个{product}！巨实用"
        ],
        "content_templates": {
            "种草型": """挖到宝了！

这个{product}真的超好用！

{selling_points}

用了就回不去了！
{price}超值，左下角链接~""",
            "测评型": """【真实测评】{product}

价格：{price}

使用感受：
{selling_points}

用了1个月，真的香！

想入手的点左下角~""",
            "干货型": """家居好物 | {product}

选购要点：
{selling_points}

这款亲测好用！

{price}性价比超高，左下角链接~"""
        },
        "tag_templates": [
            "家居好物", "提升幸福感", "实用好物", "收纳神器", "平价好物",
            "租房好物", "宿舍好物", "家居收纳", "生活好物", "好物分享"
        ],
        "color_scheme": {
            "primary": "#5D7A3D",
            "secondary": "#F5F2ED",
            "accent": "#E8E4D9"
        }
    },
    
    "大健康": {
        "keywords": ["养生", "健康", "保健品", "滋补", " wellness", "年轻人养生"],
        "title_templates": [
            "打工人必备！这个{product}真的有用",
            "熬夜党救星！{product}让我状态回来了",
            "90后已经开始养生了！{product}真香"
        ],
        "content_templates": {
            "种草型": """打工人必备！

这个{product}真的绝了！

{selling_points}

坚持喝了一个月，状态明显好了！
{price}超值，左下角链接~""",
            "测评型": """【真实测评】{product}

价格：{price}

使用感受：
{selling_points}

总体：⭐⭐⭐⭐⭐

想入手的点左下角~""",
            "干货型": """养生干货 | {product}怎么选

选购要点：
{selling_points}

这款亲测有效！

{price}性价比超高，左下角链接~"""
        },
        "tag_templates": [
            "养生", "健康养生", "打工人必备", "熬夜党", "保健品",
            "滋补", " wellness", "年轻人养生", "健康好物", "养生日常"
        ],
        "color_scheme": {
            "primary": "#48BB78",
            "secondary": "#F0FFF4",
            "accent": "#C6F6D5"
        }
    },
    
    "美妆护肤": {
        "keywords": ["护肤", "美妆", "平价", "学生党", "好用", "种草"],
        "title_templates": [
            "挖到宝！{price}的{product}太好用了",
            "平价好物！这个{product}真的绝了",
            "学生党必入！{product}性价比超高"
        ],
        "content_templates": {
            "种草型": """挖到宝了姐妹们！

这个{product}真的绝了！

{selling_points}

用了一个月，效果真的明显！
{price}超值，左下角链接~""",
            "测评型": """【真实测评】{product}

价格：{price}

使用感受：
{selling_points}

总体：⭐⭐⭐⭐⭐

想入手的点左下角~""",
            "干货型": """护肤干货 | {product}怎么选

选购要点：
{selling_points}

这款亲测好用！

{price}性价比超高，左下角链接~"""
        },
        "tag_templates": [
            "护肤", "美妆", "平价好物", "学生党", "种草",
            "护肤分享", "美妆分享", "好物推荐", "平价护肤", "护肤测评"
        ],
        "color_scheme": {
            "primary": "#ED64A6",
            "secondary": "#FFF5F7",
            "accent": "#FED7E2"
        }
    },
    
    "3C数码": {
        "keywords": ["数码", "科技", "实用", "高颜值", "性价比"],
        "title_templates": [
            "数码好物！这个{product}真的绝了",
            "挖到宝！{price}的{product}太好用了",
            "科技感满满！{product}超实用"
        ],
        "content_templates": {
            "种草型": """数码控必入！

这个{product}真的绝了！

{selling_points}

用了就回不去了！
{price}超值，左下角链接~""",
            "测评型": """【真实测评】{product}

价格：{price}

使用感受：
{selling_points}

总体：⭐⭐⭐⭐⭐

想入手的点左下角~""",
            "干货型": """数码干货 | {product}怎么选

选购要点：
{selling_points}

这款亲测好用！

{price}性价比超高，左下角链接~"""
        },
        "tag_templates": [
            "数码", "科技", "好物推荐", "数码好物", "实用",
            "高颜值", "性价比", "数码测评", "科技好物", "数码分享"
        ],
        "color_scheme": {
            "primary": "#3182CE",
            "secondary": "#EBF8FF",
            "accent": "#BEE3F8"
        }
    },
    
    "国潮文创": {
        "keywords": ["国潮", "文创", "中国风", "传统文化", "设计", "原创"],
        "title_templates": [
            "国潮崛起！这个{product}太美了",
            "中国风YYDS！{product}真的绝了",
            "文创好物！{product}超有设计感"
        ],
        "content_templates": {
            "种草型": """国潮控必入！

这个{product}真的绝了！

{selling_points}

中国风设计太美了！
{price}超值，左下角链接~""",
            "测评型": """【真实测评】{product}

价格：{price}

设计亮点：
{selling_points}

总体：⭐⭐⭐⭐⭐

想入手的点左下角~""",
            "干货型": """文创干货 | {product}怎么选

选购要点：
{selling_points}

这款设计超赞！

{price}性价比超高，左下角链接~"""
        },
        "tag_templates": [
            "国潮", "文创", "中国风", "传统文化", "设计",
            "原创", "文创好物", "国潮风", "文化", "好物推荐"
        ],
        "color_scheme": {
            "primary": "#C53030",
            "secondary": "#FFF5F5",
            "accent": "#FED7D7"
        }
    },
    
    "文玩珠宝": {
        "keywords": ["文玩", "珠宝", "手串", "翡翠", "收藏", "品质"],
        "title_templates": [
            "文玩入门！这个{product}真的绝了",
            "品质好物！{product}超值",
            "收藏级！{product}太美了"
        ],
        "content_templates": {
            "种草型": """文玩爱好者必入！

这个{product}真的绝了！

{selling_points}

品质真的没得说！
{price}超值，左下角链接~""",
            "测评型": """【真实测评】{product}

价格：{price}

品质评价：
{selling_points}

总体：⭐⭐⭐⭐⭐

想入手的点左下角~""",
            "干货型": """文玩干货 | {product}怎么选

选购要点：
{selling_points}

这款品质超赞！

{price}性价比超高，左下角链接~"""
        },
        "tag_templates": [
            "文玩", "珠宝", "手串", "翡翠", "收藏",
            "品质", "文玩好物", "珠宝分享", "收藏级", "好物推荐"
        ],
        "color_scheme": {
            "primary": "#744210",
            "secondary": "#FFFAF0",
            "accent": "#FBD38D"
        }
    },
    
    "水果生鲜": {
        "keywords": ["水果", "生鲜", "产地", "新鲜", "助农", "应季"],
        "title_templates": [
            "产地直发！这个{product}太新鲜了",
            "助农好物！{product}真的甜",
            "应季水果！{product}超好吃"
        ],
        "content_templates": {
            "种草型": """水果控必入！

这个{product}真的绝了！

{selling_points}

新鲜程度满分！
{price}超值，左下角链接~""",
            "测评型": """【真实测评】{product}

价格：{price}

口感评价：
{selling_points}

总体：⭐⭐⭐⭐⭐

想入手的点左下角~""",
            "干货型": """水果干货 | {product}怎么选

选购要点：
{selling_points}

这款口感超赞！

{price}性价比超高，左下角链接~"""
        },
        "tag_templates": [
            "水果", "生鲜", "产地直发", "新鲜", "助农",
            "应季水果", "水果推荐", "生鲜好物", "美食", "好物推荐"
        ],
        "color_scheme": {
            "primary": "#38A169",
            "secondary": "#F0FFF4",
            "accent": "#9AE6B4"
        }
    },
    
    "读书": {
        "keywords": ["读书", "阅读", "书单", "成长", "自我提升"],
        "title_templates": [
            "这本书真的绝了！{product}必读",
            "挖到宝！{product}让我受益匪浅",
            "读书分享！{product}值得推荐"
        ],
        "content_templates": {
            "种草型": """读书爱好者必入！

这本{product}真的绝了！

{selling_points}

读完收获满满！
{price}超值，左下角链接~""",
            "测评型": """【真实测评】{product}

价格：{price}

内容评价：
{selling_points}

总体：⭐⭐⭐⭐⭐

想入手的点左下角~""",
            "干货型": """读书干货 | {product}怎么选

选购要点：
{selling_points}

这本内容超赞！

{price}性价比超高，左下角链接~"""
        },
        "tag_templates": [
            "读书", "阅读", "书单", "成长", "自我提升",
            "读书分享", "好书推荐", "读书心得", "阅读分享", "好书"
        ],
        "color_scheme": {
            "primary": "#805AD5",
            "secondary": "#FAF5FF",
            "accent": "#E9D8FD"
        }
    }
}


def get_industry_list():
    """获取所有行业列表"""
    return list(ALL_INDUSTRIES.keys())


def get_industry_template(industry_name: str):
    """获取行业模板"""
    return ALL_INDUSTRIES.get(industry_name)


def get_all_industries_count():
    """获取行业总数"""
    return len(ALL_INDUSTRIES)
