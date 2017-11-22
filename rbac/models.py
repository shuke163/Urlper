from django.db import models


class Menu(models.Model):
    """
    菜单表
    """
    title = models.CharField(max_length=32, verbose_name="菜单标题")

    class Meta:
        verbose_name_plural = "菜单表"

    def __str__(self):
        return self.title


class Group(models.Model):
    """
    权限组
    """
    caption = models.CharField(max_length=32, verbose_name="组名称")
    menu = models.ForeignKey(to="Menu", default=1, blank=True, verbose_name="所属菜单")

    class Meta:
        verbose_name_plural = "权限组"

    def __str__(self):
        return self.caption


class Permission(models.Model):
    """
    权限表
    """
    title = models.CharField(max_length=32, verbose_name="标题")
    url = models.CharField(max_length=128, verbose_name="含正则的URL")
    menu_gp = models.ForeignKey(to="Permission", null=True, blank=True, verbose_name="默认选中的组内权限ID", related_name="pm")
    code = models.CharField(max_length=16, verbose_name="权限码")
    group = models.ForeignKey(to="Group", blank=True, verbose_name="所属组")

    class Meta:
        verbose_name_plural = "权限表"

    def __str__(self):
        return self.title


class User(models.Model):
    """
    用户表
    """
    username = models.CharField(max_length=32, verbose_name="用户名")
    password = models.CharField(max_length=64, verbose_name="密码")
    email = models.CharField(max_length=32, verbose_name="邮箱")
    roles = models.ManyToManyField(to="Role", blank=True, verbose_name="用户关联的角色")

    class Meta:
        verbose_name_plural = "用户表"

    def __str__(self):
        return self.username


class Role(models.Model):
    """
    角色表
    """
    title = models.CharField(max_length=32, verbose_name="角色名称")
    permissions = models.ManyToManyField(to="Permission", blank=True, verbose_name="角色关联的权限")

    class Meta:
        verbose_name_plural = "角色表"

    def __str__(self):
        return self.title
