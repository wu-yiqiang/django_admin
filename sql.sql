use django_admin;
-- user表数据
insert into `user` (`id`, `username`, `password`, `avatar`, `email`, `phone_number`, `login_date`, `status`,
                        `create_time`, `update_time`, `remark`, `is_deleted`)
values ('1', 'Administrator', '1234@Abcd', 'http://192.168.1.222:8000/storage/avatar/20250625173831.jpeg', 'Administrator@outlook.com', '18862857104', '2024-08-08', '1',
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
       (2, '系统管理', 'systems', NULL, 2, '/systems', 1, 'systems', '2024-07-04', '2024-07-04', '系统管理目录', 0),
       (3, '数据管理', 'monitor', NULL, 3, '/datas',1, 'datas', '2024-07-04', '2024-07-04', '数据管理目录', 0),
       (4, '用户管理', 'users', 2, 1, '/systems/users', 2, 'users', '2024-07-04', '2024-07-04',
        '用户管理菜单', 0),
       (5, '角色管理', 'roles', 2, 2, '/systems/roles', 2, 'roles', '2024-07-04',
        '2024-07-04', '角色管理菜单', 0),
       (6, '菜单管理', 'menus', 2, 3, '/systems/menus', 2, 'menus', '2024-07-04',
        '2024-07-04', '菜单管理菜单', 0),
        (7, '按钮管理', 'buttons', 2, 4, '/systems/buttons', 2, 'buttons', '2024-07-04',
        '2024-07-04', '按钮管理菜单', 0),
         (8, '字典管理', 'dictionarys', 2, 5, '/systems/dictionarys', 2, 'dictionarys', '2024-07-04',
        '2024-07-04', '字典管理菜单', 0),
        (9, '接口管理', 'intefaces', 2, 6, '/systems/intefaces', 2, 'intefaces', '2024-07-04',
        '2024-07-04', '接口管理菜单', 0),
       (10, '部门管理', 'tree', 3, 1, '/datas/departments', 2, 'departments', '2024-07-04', '2024-07-04',
        '部门管理菜单', 0),
       (11, '岗位管理', 'post', 3, 2, '/datas/positions',  2, 'positions', '2024-07-04', '2024-07-04', '岗位管理菜单', 0),
       (12, '公司管理', 'post', 3, 3, '/datas/companys', 2, 'companys', '2024-07-04', '2024-07-04', '公司管理菜单', 0),
       (13, '共享中心', 'shares', NULL, 3, '/shares',1, 'shares', '2024-07-04', '2024-07-04', '共享中心目录', 0),
       (14, '文件共享', 'files', 13, 3, '/shares/files',1, 'files', '2024-07-04', '2024-07-04', '文件共享菜单', 0);



 -- 按钮表
insert into `button` (`id`, `name`, `code`, `create_time`, `update_time`, `remark`, `is_deleted`)
values (1, '用户查询', 'system:user:query', '2024-07-04', '2024-07-04', '用户查询权限', 0),
       (2, '用户导出', 'system:user:export', '2024-07-04', '2024-07-04', '用户导出权限', 0),
       (3, '用户创建', 'system:user:create', '2024-07-04', '2024-07-04', '用户创建权限', 0),
       (4, '用户编辑', 'system:user:edit', '2024-07-04', '2024-07-04', '用户编辑权限', 0),
       (5, '用户删除','system:user:delete', '2024-07-04', '2024-07-04', '用户删除权限', 0),
       (6, '角色查询','system:role:query', '2024-07-04', '2024-07-04', '角色查询权限', 0),
       (7, '角色创建','system:role:create', '2024-07-04', '2024-07-04', '角色创建权限', 0),
       (8, '角色编辑','system:role:edit', '2024-07-04', '2024-07-04', '角色编辑权限', 0),
       (9, '角色删除','system:role:delete', '2024-07-04', '2024-07-04', '角色删除权限', 0),
       (10, '角色导出','system:role:export', '2024-07-04', '2024-07-04', '角色导出权限', 0);


 -- 接口表
insert into `inteface`(`id`, `name`, `type`, `path`, `create_time`, `update_time`, `remark`, `is_deleted`)
values (1, '查询用户列表', 1, '/user/page','2024-07-04', '2024-07-04', '查询用户列表', 0),
       (2, '添加用户', 2,'/user/create', '2024-07-04', '2024-07-04', '添加用户', 0),
       (3, '删除用户', 3, '/user/delete','2024-07-04', '2024-07-04', '删除用户', 0),
       (4, '编辑用户', 2,'/user/update', '2024-07-04', '2024-07-04', '编辑用户', 0),
       (5, '查询全量用户', 1,'/user/list', '2024-07-04', '2024-07-04', '查询全量用户', 0),
       (6, '查询用户详情',1,'/user/detail', '2024-07-04', '2024-07-04', '查询用户详情', 0),
       (7, '查询角色列表',1,'/role/page', '2024-07-04', '2024-07-04', '查询角色列表', 0),
       (8, '添加角色',2,'/role/create', '2024-07-04', '2024-07-04', '添加角色', 0),
       (9, '删除角色',3,'/role/delete', '2024-07-04', '2024-07-04', '删除角色', 0),
       (10, '编辑角色',2,'/role/update', '2024-07-04', '2024-07-04', '编辑角色', 0),
       (11, '查询全量角色', 1,'/role/list', '2024-07-04', '2024-07-04', '查询全量角色', 0),
       (12, '查询角色详情',1,'/role/detail', '2024-07-04', '2024-07-04', '查询角色详情', 0),
       (13, '查询菜单列表',1,'/menu/page', '2024-07-04', '2024-07-04', '查询菜单列表', 0),
       (14, '添加菜单',2,'/menu/create', '2024-07-04', '2024-07-04', '添加菜单', 0),
       (15, '删除菜单',3,'/menu/delete', '2024-07-04', '2024-07-04', '删除菜单', 0),
       (16, '编辑菜单',2,'/menu/update', '2024-07-04', '2024-07-04', '编辑菜单', 0),
       (17, '查询全量菜单', 1,'/menu/list', '2024-07-04', '2024-07-04', '查询全量菜单', 0),
       (18, '查询菜单详情',1,'/menu/detail', '2024-07-04', '2024-07-04', '查询菜单详情', 0),
       (19, '查询菜单树形列表',1,'/menu/treeLists', '2024-07-04', '2024-07-04', '查询菜单树形列表', 0),
       (20, '查询接口列表',1,'/inteface/page', '2024-07-04', '2024-07-04', '查询接口列表', 0),
       (21, '添加接口',2,'/inteface/create', '2024-07-04', '2024-07-04', '添加接口', 0),
       (22, '删除接口',3,'/inteface/delete', '2024-07-04', '2024-07-04', '删除接口', 0),
       (23, '编辑接口',2,'/inteface/update', '2024-07-04', '2024-07-04', '编辑接口', 0),
       (24, '查询全量接口', 1,'/inteface/list', '2024-07-04', '2024-07-04', '查询全量接口', 0),
       (25, '查询接口详情',1,'/inteface/detail', '2024-07-04', '2024-07-04', '查询菜单详情', 0),
       (26, '查询字典列表',1,'/dictionary/page', '2024-07-04', '2024-07-04', '查询字典列表', 0),
       (27, '添加字典',2,'/dictionary/create', '2024-07-04', '2024-07-04', '添加字典', 0),
       (28, '删除字典',3,'/dictionary/delete', '2024-07-04', '2024-07-04', '删除字典', 0),
       (29, '编辑字典',2,'/dictionary/update', '2024-07-04', '2024-07-04', '编辑字典', 0),
       (30, '查询全量字典类型', 1,'/dictionary/types', '2024-07-04', '2024-07-04', '查询全量字典类型', 0),
       (31, '查询字典详情',1,'/dictionary/detail', '2024-07-04', '2024-07-04', '查询字典详情', 0),
       (32, '查询按钮列表',1,'/button/page', '2024-07-04', '2024-07-04', '查询按钮列表', 0),
       (33, '添加按钮',2,'/button/create', '2024-07-04', '2024-07-04', '添加按钮', 0),
       (34, '删除按钮',3,'/button/delete', '2024-07-04', '2024-07-04', '删除按钮', 0),
       (35, '编辑按钮',2,'/button/update', '2024-07-04', '2024-07-04', '编辑按钮', 0),
       (36, '编辑按钮',2,'/button/update', '2024-07-04', '2024-07-04', '编辑按钮', 0),
       (37, '查询全量按钮', 1,'/button/list', '2024-07-04', '2024-07-04', '查询全量按钮', 0),
       (38, '查询按钮详情',1,'/button/detail', '2024-07-04', '2024-07-04', '查询按钮详情', 0);


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

-- 角色按钮表
insert into `role_buttons`(`id`,  `role_id`, `button_id`)
values (1, 1, 1),
       (2, 1, 2),
       (3, 1, 3),
       (4, 1, 4),
       (5, 1, 5),
       (6, 1, 6),
       (7, 1, 7),
       (8, 1, 8),
       (9, 1, 9),
       (10, 1, 10);

 -- 角色接口表
insert into `role_intefaces`(`id`,  `role_id`, `inteface_id`)
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
       (14, 1, 14),
       (15, 1, 15),
       (16, 1, 16),
       (17, 1, 17),
       (18, 1, 18),
       (19, 1, 19),
       (20, 1, 20),
       (21, 1, 21),
       (22, 1, 22),
       (23, 1, 23),
       (24, 1, 24),
       (25, 1, 25),
       (26, 1, 26),
       (27, 1, 27),
       (28, 1, 28),
       (29, 1, 29),
       (30, 1, 30),
       (31, 1, 31),
       (32, 1, 32),
       (33, 1, 33),
       (34, 1, 34),
       (35, 1, 35),
       (36, 1, 36),
       (37, 1, 37),
       (38, 1, 38);




-- 菜单按钮表
insert into `menu_buttons`(`id`, `menu_id`,`button_id`)
values (1, 4, 1),
       (2, 4, 2),
       (3, 4, 3),
       (4, 4, 4),
       (5, 4, 5),
       (6, 5, 6),
       (7, 5, 7),
       (8, 5, 8),
       (9, 5, 9),
       (10, 5, 10);


-- 菜单接口表
insert into `menu_intefaces`(`id`, `menu_id`,`inteface_id`)
values (1, 4, 1),
       (2, 4, 2),
       (3, 4, 3),
       (4, 4, 4),
       (5, 4, 5),
       (6, 5, 6),
       (7, 5, 7),
       (8, 5, 8),
       (9, 5, 9),
       (10, 5, 10);

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

 -- 文件表
insert into `net_disk` (`id`, `url`,`parentId`,`fileName`,  `fileSize`,  `isFold`, `create_time`, `update_time`, `remark`, `is_deleted`)
values (1, 'http://192.168.1.222:8000/storage/netdisk/2022_PDF.pdf',NULL, '2022_pdf.pdf','140kb', FALSE,'2024-07-04', '2024-07-04', '文件', 0),
       (2, 'http://192.168.1.222:8000/storage/netdisk/物体的缩放.mp4', NULL,'物体的缩放.mp4', '200MB',FALSE, '2024-07-04', '2024-07-04', '文件', 0),
       (3, 'http://192.168.1.222:8000/storage/netdisk/新建文件夹',NULL,'新建文件夹', '200MB',TRUE, '2024-07-04', '2024-07-04', '目录', 0);


