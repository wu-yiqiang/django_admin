-- user表数据
insert into `user` (`id`, `username`, `password`, `avatar`, `email`, `phone_number`, `login_date`, `status`,
                        `create_time`, `update_time`, `remark`, `is_deleted`)
values ('1', 'Administrator', '1234@Abcd', '20240906202303.jpg', 'Administrator@outlook.com', '18862857104', '2024-08-08', '1',
        '2024-08-08', '2024-08-08', '超级管理员', FALSE);
insert into `user` (`id`, `username`, `password`, `avatar`, `email`, `phone_number`, `login_date`, `status`,
                        `create_time`, `update_time`, `remark`,`is_deleted`)
values ('3', 'Tom', '123456', '20240808230603.jpg', 'caofeng2014@126.com', '18862857104', '2024-08-08', '0', '2024-08-08',
        '2024-08-14', '测试用户', FALSE);
insert into `user` (`id`, `username`, `password`, `avatar`, `email`, `phone_number`, `login_date`, `status`,
                        `create_time`, `update_time`, `remark`, `is_deleted`)
values ('6', 'Nacy', '123456', '20240808230603.jpg', 'Nacy@outlook.com', NULL, NULL, '1', NULL, NULL, NULL,FALSE);
insert into `user` (`id`, `username`, `password`, `avatar`, `email`, `phone_number`, `login_date`, `status`,
                        `create_time`, `update_time`, `remark`,`is_deleted`)
values ('7', 'Aliyamama', '123456', '20240808230603.jpg', 'Aliyamama@outlook.com', NULL, NULL, '1', NULL, NULL, NULL,FALSE);
insert into `user` (`id`, `username`, `password`, `avatar`, `email`, `phone_number`, `login_date`, `status`,
                        `create_time`, `update_time`, `remark`,`is_deleted`)
values ('8', 'Alsaadi', '123456', '20240808230603.jpg', 'Alsaadi@outlook.com', NULL, NULL, '0', NULL, NULL, NULL,FALSE);
insert into `user` (`id`, `username`, `password`, `avatar`, `email`, `phone_number`, `login_date`, `status`,
                        `create_time`, `update_time`, `remark`,`is_deleted`)
values ('11', 'Mouhammad', '123456', '20240808230603.jpg', 'Mouhammad@outlook.com', NULL, NULL, '1', NULL, NULL, NULL,FALSE);
insert into `user` (`id`, `username`, `password`, `avatar`, `email`, `phone_number`, `login_date`, `status`,
                        `create_time`, `update_time`, `remark`,`is_deleted`)
values ('14', 'Yassir', '123456', 'default.jpg', 'caofeng2014@126.com', '18862857104', NULL, '1', '2024-08-13', NULL,
        '33',FALSE);
insert into `user` (`id`, `username`, `password`, `avatar`, `email`, `phone_number`, `login_date`, `status`,
                        `create_time`, `update_time`, `remark`,`is_deleted`)
values ('15', 'jack', '123456', 'default.jpg', 'caofeng2014@126.com', '18862857104', NULL, '1', '2024-08-13',
        '2024-09-06', '禁用用户测试4',FALSE);
insert into `user` (`id`, `username`, `password`, `avatar`, `email`, `phone_number`, `login_date`, `status`,
                        `create_time`, `update_time`, `remark`,`is_deleted`)
values ('16', 'Zoe', '123456', 'default.jpg', '1@126.com', '18862857104', NULL, '1', '2024-08-18', '2024-08-18',
        '115',FALSE);
insert into `user` (`id`, `username`, `password`, `avatar`, `email`, `phone_number`, `login_date`, `status`,
                        `create_time`, `update_time`, `remark`,`is_deleted`)
values ('17', 'marry', '123456', 'default.jpg', '111@qq.com', '15586521012', NULL, '1', '2024-09-05', NULL, '555',FALSE);
insert into `user` (`id`, `username`, `password`, `avatar`, `email`, `phone_number`, `login_date`, `status`,
                        `create_time`, `update_time`, `remark`,`is_deleted`)
values ('18', 'sutter.wu', '1234@Abcd', 'default.jpg', 'sutter.wu@outlook.com', '15586521012', NULL, '1', '2024-09-05', NULL, '555',FALSE);



-- 角色表
insert into `role` (`id`, `name`, `code`, `create_time`, `update_time`, `remark`, `is_deleted`)
values (1, '超级管理员', 'administrator', '2024-07-04', '2024-07-04', '拥有系统最高权限',0),
       (2, '普通角色', 'user', '2024-07-04', '2024-07-04', '普通角色',0),
       (3, '测试角色', 'test', '2024-07-04', '2024-07-04', '测试角色', 0),
       (4, '系统部管理员', 'system_admin', '2024-07-04', '2024-07-04', NULL, 0),
       (5, '运维部管理员', 'maintenance_admin', '2024-07-04', '2024-07-04', NULL, 0),
       (6, '开发部管理员', 'develop_admin', '2024-07-04', '2024-07-04', NULL, 0);

-- 菜单表
insert into `menu` (`id`, `name`, `icon`, `parent_id`, `order_num`, `path`, `menu_type`, `code`,
                        `create_time`, `update_time`, `remark`, `is_deleted`)
values (1, '个人中心', 'personal', 0, 1, '/personal', '1', 'setting', '2024-07-04', '2024-07-04', '个人中心目录', 0),
       (2, '系统管理', 'system', 0, 2, '/setting', '1', 'setting', '2024-07-04', '2024-07-04', '系统管理目录', 0),
       (3, '业务管理', 'monitor', 0, 3, '/mainData','1', 'mainData', '2024-07-04', '2024-07-04', '业务管理目录', 0),
       (4, '用户管理', 'user', 1, 1, '/setting/user', '2', 'user', '2024-07-04', '2024-07-04',
        '用户管理菜单', 0),
       (5, '角色管理', 'peoples', 1, 2, '/setting/role', '2', 'role', '2024-07-04',
        '2024-07-04', '角色管理菜单', 0),
       (6, '菜单管理', 'treetable', 1, 3, '/setting/menu', '2', 'menu', '2024-07-04',
        '2024-07-04', '菜单管理菜单', 0),
       (7, '部门管理', 'tree', 2, 1, '/mainData/department', '2', 'department', '2024-07-04', '2024-07-04',
        '部门管理菜单', 0),
       (8, '岗位管理', 'post', 2, 2, '/mainData/position',  '2', 'position', '2024-07-04', '2024-07-04', '岗位管理菜单', 0),
       (9, '公司管理', 'post', 2, 3, '/mainData/company', '2', 'company', '2024-07-04', '2024-07-04', '公司管理菜单', 0);

 -- 按钮表
insert into `button` (`id`, `name`, `code`, `create_time`, `update_time`, `remark`, `is_deleted`)
values (1, '查询', '1', '2024-07-04', '2024-07-04', '查询权限', 0),
       (2, '导出', '10', '2024-07-04', '2024-07-04', '导出权限', 0),
       (3, '创建', '100', '2024-07-04', '2024-07-04', '创建权限', 0),
       (4, '编辑', '1000', '2024-07-04', '2024-07-04', '编辑权限', 0),
       (5, '删除','10000', '2024-07-04', '2024-07-04', '删除权限', 0);


 -- 接口表
insert into `inteface`(`id`, `name`, `type`, `path`, `create_time`, `update_time`, `remark`, `is_deleted`)
values (1, '查询用户列表', 1, '/user/page','2024-07-04', '2024-07-04', '查询用户列表', 0),
       (2, '添加用户', 2,'/user/create', '2024-07-04', '2024-07-04', '添加用户', 0),
       (3, '删除用户', 3, '/user/delete','2024-07-04', '2024-07-04', '删除用户', 0),
       (4, '编辑用户', 2,'/user/update', '2024-07-04', '2024-07-04', '编辑用户', 0),
       (5, '查询用户详情',1,'/user/detail', '2024-07-04', '2024-07-04', '查询用户详情', 0);

-- 用户角色表
insert into `user_roles`(`id`, `role_id`, `user_id`)
values (1, 1, 1),
       (2, 2, 1),
       (3, 3, 1),
       (4, 4, 1),
       (5, 5, 1),
       (6, 6, 1);

-- 角色菜单表
insert into `role_menus`(`id`, `menu_id`, `role_id`)
values (1, 1, 1),
       (2, 2, 1),
       (3, 3, 1),
       (4, 4, 1),
       (5, 5, 1),
       (6, 6, 1),
       (7, 7, 1),
       (8, 8, 1),
       (9, 9, 1);

-- 角色按钮表
insert into `role_buttons`(`id`, `button_id`, `role_id`)
values (1, 1, 1),
       (2, 2, 1),
       (3, 3, 1),
       (4, 4, 1),
       (5, 5, 1);


-- 角色接口表
insert into `role_intefaces`(`id`, `inteface_id`, `role_id`)
values (1, 1, 1),
       (2, 2, 1),
       (3, 3, 1),
       (4, 4, 1),
       (5, 5, 1);




--维修表--
insert into `maintains` (`id`, `device_name`, `applyer`, `maintainer`, `subject`,
                        `create_time`, `update_time`, `remark`, `is_deleted`)
values (1, '水箱', '008672323', '008672323', "水箱漏水", '2024-07-04', '2024-07-04', '水箱左下角有破洞', 0),
       (2, '加压器', '008672323', '008672323', "水箱漏水", '2024-07-04', '2024-07-04', '水箱左下角有破洞', 0),
       (3, '发电机', '008672323', '008672323', "发电机不工作", '2024-07-04', '2024-07-04', '发电机无法启动', 0),
       (4, '监控', '008672323', '008672325', "监控器异常", '2024-07-04', '2024-07-04', '监控器无法查看监控，显示雪花状', 0),
       (5, '热水器', '008672323', '008672323', "热水器没有热水", '2024-07-04', '2024-07-04', '热水器打开没有热水，只流出冷水', 0);