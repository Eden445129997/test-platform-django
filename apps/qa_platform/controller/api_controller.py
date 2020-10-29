#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 模型
from apps.qa_platform.models.domain import api
# 自定义模型视图
from apps.common.views import CustomModelViewSet
# 序列化
from apps.qa_platform import serializers

class ApiViews(CustomModelViewSet):
    """接口表"""
    queryset = api.Api.objects.all()
    serializer_class = serializers.ApiSerializer

    # 精确匹配
    # project_id、content_type、method、is_status
    # 模糊查询字段
    search_fields = ('api_name','path',)
