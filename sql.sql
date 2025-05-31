-- user表数据
insert into `user` (`id`, `username`, `password`, `avatar`, `email`, `phone_number`, `login_date`, `status`,
                        `create_time`, `update_time`, `remark`, `is_deleted`)
values ('1', 'python222', '123456', '20240906202303.jpg', 'caofeng2014@126.com', '18862857104', '2024-08-08', '1',
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

-- 菜单表
insert into `sys_menu` (`id`, `name`, `icon`, `parent_id`, `order_num`, `path`, `menu_type`, `code`,
                        `create_time`, `update_time`, `remark`, `is_deleted`)
values (1, '个人中心', 'personal', 0, 1, '', '1', 'setting', '2024-07-04', '2024-07-04', '个人中心目录', 0),
       (2, '系统管理', 'system', 0, 2, '/setting', '1', 'setting', '2024-07-04', '2024-07-04', '系统管理目录', 0)
       (3, '业务管理', 'monitor', 0, 3, '/basicData',1', 'BasicData', '2024-07-04', '2024-07-04', '业务管理目录', 0),
       (4, '用户管理', 'user', 1, 1, '/setting/user', '2', 'user', '2024-07-04', '2024-07-04',
        '用户管理菜单', 0),
       (5, '角色管理', 'peoples', 1, 2, '/setting/role', '2', 'role', '2024-07-04',
        '2024-07-04', '角色管理菜单', 0),
       (6, '菜单管理', 'treetable', 1, 3, '/setting/menu', '2', 'menu', '2024-07-04',
        '2024-07-04', '菜单管理菜单', 0),
       (7, '部门管理', 'tree', 2, 1, '/basicData/department', '2', 'department', '2024-07-04', '2024-07-04',
        '部门管理菜单', 0),
       (8, '岗位管理', 'post', 2, 2, '/basicData/position',  '2', 'position', '2024-07-04', '2024-07-04', '岗位管理菜单', 0);
       (9, '公司管理', 'post', 2, 3, '/basicData/company', '2', 'company', '2024-07-04', '2024-07-04', '公司管理菜单', 0);

-- 角色表
insert into `role`(`id`, `name`, `code`, `create_time`, `update_time`, `remark`, `is_deleted`)
values (1, '超级管理员', 'super_admin', '2024-07-04', '2024-07-04', '拥有系统最高权限',0),
       (2, '普通角色', 'user', '2024-07-04', '2024-07-04', '普通角色',0),
       (3, '测试角色', 'test', '2024-07-04', '2024-07-04', '测试角色', 0),
       (4, '系统部管理员', 'system_admin', '2024-07-04', '2024-07-04', NULL, 0),
       (5, '运维部管理员', 'maintenance_admin', '2024-07-04', '2024-07-04', NULL, 0),
       (6, '开发部管理员', 'develop_admin', '2024-07-04', '2024-07-04', NULL, 0);


insert into `sys_role_menu`(`id`, `menu_id`, `role_id`)
values (102, 2, 2),
       (103, 6, 2),
       (104, 7, 2),
       (106, 1, 1),
       (107, 3, 1),
       (108, 4, 1),
       (109, 5, 1),
       (110, 2, 1),
       (111, 6, 1),
       (112, 7, 1),
       (114, 1, 6),
       (115, 5, 6),
       (116, 2, 6),
       (117, 6, 6),
       (118, 7, 6);
insert into `user_role`(`id`, `role_id`, `user_id`)
values (1, 1, 1),
       (2, 2, 1),
       (13, 5, 6),
       (17, 2, 6),
       (18, 3, 6),
       (19, 20, 6),
       (20, 2, 8),
       (21, 20, 8),
       (22, 5, 8),
       (23, 2, 17),
       (24, 2, 3),
       (25, 3, 3),
       (26, 4, 3),
       (27, 2, 15);



--维修表--
insert into `maintains` (`id`, `device_name`, `applyer`, `maintainer`, `subject`,
                        `create_time`, `update_time`, `remark`, `is_deleted`)
values (1, '水箱', '008672323', '008672323', "水箱漏水", '2024-07-04', '2024-07-04', '水箱左下角有破洞', 0),
       (2, '加压器', '008672323', '008672323', "水箱漏水", '2024-07-04', '2024-07-04', '水箱左下角有破洞', 0),
       (3, '发电机', '008672323', '008672323', "发电机不工作", '2024-07-04', '2024-07-04', '发电机无法启动', 0),
       (4, '监控', '008672323', '008672325', "监控器异常", '2024-07-04', '2024-07-04', '监控器无法查看监控，显示雪花状', 0),
       (5, '热水器', '008672323', '008672323', "热水器没有热水", '2024-07-04', '2024-07-04', '热水器打开没有热水，只流出冷水', 0);