# Generated by Django 3.0.6 on 2020-06-16 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_platform', '0003_auto_20200615_0047'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckPoint',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('case_detail_id', models.CharField(max_length=16, verbose_name='所属的case_detail')),
                ('point_object', models.CharField(max_length=64, verbose_name='检查对象，jsonpath表达式')),
                ('check_method', models.CharField(choices=[('assertEqual', 'assertEqual'), ('assertNotEqual', 'assertNotEqual'), ('assertIn', 'assertIn'), ('assertNotIn', 'assertNotIn')], max_length=16, verbose_name='校验方法')),
                ('check_value', models.TextField(verbose_name='校验的比对值')),
                ('text', models.CharField(blank=True, max_length=255, null=True, verbose_name='用例描述')),
                ('status', models.BooleanField(default=True, verbose_name='状态')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '检查点',
                'verbose_name_plural': '检查点',
                'db_table': 'tb_check_point',
            },
        ),
        migrations.AlterField(
            model_name='apitestreport',
            name='task_status',
            field=models.CharField(choices=[('等待执行', '等待执行'), ('执行中', '执行中'), ('完成', '完成'), ('失败', '失败')], max_length=16, verbose_name='任务状态（1、等待执行2、执行中3、成功4、失败）'),
        ),
        migrations.AlterField(
            model_name='apitestreportdetail',
            name='case_id',
            field=models.CharField(max_length=16, verbose_name='所属用例id'),
        ),
        migrations.AlterField(
            model_name='apitestreportdetail',
            name='report_id',
            field=models.CharField(max_length=16, verbose_name='所属报告id'),
        ),
        migrations.AlterField(
            model_name='busimodel',
            name='project_id',
            field=models.CharField(max_length=16, verbose_name='所属项目id'),
        ),
        migrations.AlterField(
            model_name='host',
            name='project_id',
            field=models.CharField(max_length=16, verbose_name='所属项目id'),
        ),
        migrations.AlterField(
            model_name='interface',
            name='busi_id',
            field=models.CharField(max_length=16, verbose_name='所属业务id'),
        ),
        migrations.AlterField(
            model_name='interface',
            name='method',
            field=models.CharField(choices=[('GET', 'GET'), ('POST', 'POST'), ('PUT', 'PUT'), ('DELETE', 'DELETE')], max_length=255, verbose_name='请求方式'),
        ),
        migrations.AlterField(
            model_name='interface',
            name='project_id',
            field=models.CharField(max_length=16, verbose_name='所属项目id'),
        ),
        migrations.AlterField(
            model_name='testcase',
            name='plan_id',
            field=models.CharField(max_length=16, verbose_name='所属计划id'),
        ),
        migrations.AlterField(
            model_name='testcasedetail',
            name='case_id',
            field=models.CharField(max_length=16, verbose_name='所属用例id'),
        ),
        migrations.AlterField(
            model_name='testcasedetail',
            name='interface_id',
            field=models.CharField(max_length=16, verbose_name='请求资源地址'),
        ),
        migrations.AlterField(
            model_name='testplan',
            name='project_id',
            field=models.CharField(max_length=16, verbose_name='所属项目id'),
        ),
    ]
