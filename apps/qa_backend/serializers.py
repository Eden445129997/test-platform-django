#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from apps.common.base_obj import BaseSerializer

from apps.qa_backend.models.domain import (
    api, api_assert, api_case_data, api_case_data_node, api_case_model,
    event, event_api_record, event_api_result, host, project, qa_case, qa_plan
)


class ProjectSerializer(BaseSerializer):
    """工程表"""
    class Meta:
        model = project.Project
        fields = "__all__"
        # exclude = ('add_time',):  除去指定的某些字段

class HostSerializer(BaseSerializer):
    """域名表"""
    class Meta:
        model = host.Host
        fields = "__all__"

class ApiSerializer(BaseSerializer):
    """接口表"""
    class Meta:
        model = api.Api
        fields = "__all__"

class QaPlanSerializer(BaseSerializer):
    """测试计划表"""
    class Meta:
        model = qa_plan.QaPlan
        fields = "__all__"

class QaCaseSerializer(BaseSerializer):
    """测试用例表"""
    class Meta:
        model = qa_case.QaCase
        fields = "__all__"

class ApiCaseModelSerializer(BaseSerializer):
    """测试细节表(测试参数表)"""
    class Meta:
        model = api_case_model.ApiCaseModel
        fields = "__all__"

class ApiCaseDataSerializer(BaseSerializer):
    """测试细节表(测试参数表)"""
    class Meta:
        model = api_case_data.ApiCaseData
        fields = "__all__"

class ApiCaseDataNodeSerializer(BaseSerializer):
    """测试细节表(测试参数表)"""
    class Meta:
        model = api_case_data_node.ApiCaseDataNode
        fields = "__all__"

class ApiAssertSerializer(BaseSerializer):
    """测试细节表(测试参数表)"""
    class Meta:
        model = api_assert.ApiAssert
        fields = "__all__"

class EventSerializer(BaseSerializer):
    """事件"""
    class Meta:
        model = event.Event
        fields = "__all__"

class EventApiRecordSerializer(BaseSerializer):
    """接口测试报告细节"""
    class Meta:
        model = event_api_record.EventApiRecord
        fields = "__all__"

class EventApiResultSerializer(BaseSerializer):
    """接口测试报告细节"""
    class Meta:
        model = event_api_result.EventApiResult
        fields = "__all__"

# class TestUserSerializer(BaseSerializer)
#     """测试ModelSerializer的功能"""
#     # 有些字段也需要序列化， 但是这些字段不在参照模型中
#     # 在这里添加额外需要序列化的字段， 即不在指定参照模型中的字段，
#     # 再直白点， 就是不在表User内的字段
#     mobile = serializers.CharFileld(label='手机号', min_length = 11, max_length = 11)
#
#     class Meta:
#         # 指明参照模型
#         model = User
#         # 指明字段， 即要序列化的字段
#         fields = '__all__'  # 所有表User中字段
#         fields = ['username', 'password', 'mobile']  # 指定字段 新添加的也可以指定
#         exclude = ['password2']  # 排除掉的字段
#         read_only_fields = ('username', 'password')  # 标明只读字段
#
#         # 添加或修改原有字段的选项残数据
#         extra_kwargs = {
#             'username': {
#                 'min_length': 5,
#                 'max_length': 20,
#                 'error_messages': {
#                     'min_length': '仅允许5-20个字段的用户',
#                     'max_length': '仅允许5-20个字段的用户',
#                 }
#             },
#             'password': {
#                 'write_only': True,
#                 'min_length': 8,
#                 'max_length': 20,
#                 'error_messages': {
#                     'min_length': '仅允许8-20个字段的密码',
#                     'max_length': '仅允许8-20个字段的密码',
#                 }
#             }
#         }