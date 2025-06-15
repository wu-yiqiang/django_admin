use django_admin;
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
values (1, '个人中心', 'personal', NULL, 1, '/personal', 2, 'personal', '2024-07-04', '2024-07-04', '个人中心菜单', 0),
       (2, '系统管理', 'settings', NULL, 2, '/settings', 1, 'settings', '2024-07-04', '2024-07-04', '系统管理目录', 0),
       (3, '数据管理', 'monitor', NULL, 3, '/datas',1, 'datas', '2024-07-04', '2024-07-04', '数据管理目录', 0),
       (4, '用户管理', 'users', 2, 1, '/settings/users', 2, 'users', '2024-07-04', '2024-07-04',
        '用户管理菜单', 0),
       (5, '角色管理', 'roles', 2, 2, '/settings/roles', 2, 'roles', '2024-07-04',
        '2024-07-04', '角色管理菜单', 0),
       (6, '菜单管理', 'menus', 2, 3, '/settings/menus', 2, 'menus', '2024-07-04',
        '2024-07-04', '菜单管理菜单', 0),
        (7, '按钮管理', 'buttons', 2, 4, '/settings/buttons', 2, 'buttons', '2024-07-04',
        '2024-07-04', '按钮管理菜单', 0),
         (8, '字典管理', 'dictionarys', 2, 5, '/settings/dictionarys', 2, 'dictionarys', '2024-07-04',
        '2024-07-04', '字典管理菜单', 0),
        (9, '接口管理', 'intefaces', 2, 6, '/settings/intefaces', 2, 'intefaces', '2024-07-04',
        '2024-07-04', '接口管理菜单', 0),
       (10, '部门管理', 'tree', 3, 1, '/datas/departments', 2, 'departments', '2024-07-04', '2024-07-04',
        '部门管理菜单', 0),
       (11, '岗位管理', 'post', 3, 2, '/datas/positions',  2, 'positions', '2024-07-04', '2024-07-04', '岗位管理菜单', 0),
       (12, '公司管理', 'post', 3, 3, '/datas/companys', 2, 'companys', '2024-07-04', '2024-07-04', '公司管理菜单', 0),
       (13, '文件管理', 'files', NULL, 3, '/files',1, 'files', '2024-07-04', '2024-07-04', '文件管理目录', 0),
       (14, '文档管理', 'documents', 13, 3, '/files/documents',1, 'documents', '2024-07-04', '2024-07-04', '文件管理菜单', 0);



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
insert into `user_roles`(`id`,`user_id`, `role_id`)
values (1, 1, 1),
       (2, 1, 2),
       (3, 1, 3),
       (4, 1, 4),
       (5, 1, 5),
       (6, 1, 6);

-- 角色菜单表
insert into `role_menus`(`id`,  `role_id`, `menu_id`)
values (1, 1, 1),
       (2, 1, 2),
       (3, 1, 3),
       (4, 1, 4),
       (5, 1, 5),
       (6, 1, 6),
       (7, 1, 7),
       (8, 1, 8),
       (9, 1, 9),
       (10, 1, 10),
       (11, 1, 11),
       (12, 1, 12),
       (13, 1, 13),
       (14, 1, 14);



-- 菜单按钮表
insert into `menu_buttons`(`id`, `menu_id`,`button_id`)
values (1, 1, 1),
       (2, 1, 2),
       (3, 1, 3),
       (4, 1, 4),
       (5, 1, 5);


-- 菜单接口表
insert into `menu_intefaces`(`id`, `menu_id`,`inteface_id`)
values (1, 1, 1),
       (2, 1, 2),
       (3, 1, 3),
       (4, 1, 4),
       (5, 1, 5);

 -- 字典表
insert into `dictionary` (`id`, `type`,`code`,  `label`,   `color`, `bgcolor`, `create_time`, `update_time`, `remark`, `is_deleted`)
values (1, 'status', 0,'禁用', '','','2024-07-04', '2024-07-04', '禁用', 0),
       (2, 'status', 1, '启用','','', '2024-07-04', '2024-07-04', '启用', 0),
       (3, 'menuType',1, '目录','','', '2024-07-04', '2024-07-04', '目录', 0),
       (4, 'menuType',2, '菜单','','', '2024-07-04', '2024-07-04', '菜单', 0),
       (5, 'intefaceType',1,'GET','','', '2024-07-04', '2024-07-04', 'GET', 0),
       (6, 'intefaceType',2,'POST','','', '2024-07-04', '2024-07-04', 'POST', 0),
       (7, 'intefaceType',3,'DELETE','','', '2024-07-04', '2024-07-04', 'DELETE', 0),
       (8, 'intefaceType',4,'PUT','','', '2024-07-04', '2024-07-04', 'PUT', 0);


