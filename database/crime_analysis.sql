-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 23, 2021 at 04:20 PM
-- Server version: 10.4.20-MariaDB
-- PHP Version: 7.3.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `crime_analysis`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can add permission', 2, 'add_permission'),
(5, 'Can change permission', 2, 'change_permission'),
(6, 'Can delete permission', 2, 'delete_permission'),
(7, 'Can add group', 3, 'add_group'),
(8, 'Can change group', 3, 'change_group'),
(9, 'Can delete group', 3, 'delete_group'),
(10, 'Can add user', 4, 'add_user'),
(11, 'Can change user', 4, 'change_user'),
(12, 'Can delete user', 4, 'delete_user'),
(13, 'Can add content type', 5, 'add_contenttype'),
(14, 'Can change content type', 5, 'change_contenttype'),
(15, 'Can delete content type', 5, 'delete_contenttype'),
(16, 'Can add session', 6, 'add_session'),
(17, 'Can change session', 6, 'change_session'),
(18, 'Can delete session', 6, 'delete_session'),
(19, 'Can add user_reg', 7, 'add_user_reg'),
(20, 'Can change user_reg', 7, 'change_user_reg'),
(21, 'Can delete user_reg', 7, 'delete_user_reg'),
(22, 'Can add station_details', 8, 'add_station_details'),
(23, 'Can change station_details', 8, 'change_station_details'),
(24, 'Can delete station_details', 8, 'delete_station_details'),
(25, 'Can add user_complaints', 9, 'add_user_complaints'),
(26, 'Can change user_complaints', 9, 'change_user_complaints'),
(27, 'Can delete user_complaints', 9, 'delete_user_complaints'),
(28, 'Can add criminal_details', 10, 'add_criminal_details'),
(29, 'Can change criminal_details', 10, 'change_criminal_details'),
(30, 'Can delete criminal_details', 10, 'delete_criminal_details');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(8, 'higher_officer', 'station_details'),
(10, 'police', 'criminal_details'),
(6, 'sessions', 'session'),
(9, 'user', 'user_complaints'),
(7, 'user', 'user_reg');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2021-10-11 09:59:02.630859'),
(2, 'auth', '0001_initial', '2021-10-11 09:59:11.056640'),
(3, 'admin', '0001_initial', '2021-10-11 09:59:12.869140'),
(4, 'admin', '0002_logentry_remove_auto_add', '2021-10-11 09:59:13.021484'),
(5, 'contenttypes', '0002_remove_content_type_name', '2021-10-11 09:59:14.001953'),
(6, 'auth', '0002_alter_permission_name_max_length', '2021-10-11 09:59:14.861328'),
(7, 'auth', '0003_alter_user_email_max_length', '2021-10-11 09:59:14.994140'),
(8, 'auth', '0004_alter_user_username_opts', '2021-10-11 09:59:15.037109'),
(9, 'auth', '0005_alter_user_last_login_null', '2021-10-11 09:59:15.462890'),
(10, 'auth', '0006_require_contenttypes_0002', '2021-10-11 09:59:15.482421'),
(11, 'auth', '0007_alter_validators_add_error_messages', '2021-10-11 09:59:15.513671'),
(12, 'auth', '0008_alter_user_username_max_length', '2021-10-11 09:59:15.619140'),
(13, 'auth', '0009_alter_user_last_name_max_length', '2021-10-11 09:59:15.736328'),
(14, 'sessions', '0001_initial', '2021-10-11 09:59:16.908203'),
(15, 'user', '0001_initial', '2021-10-11 09:59:17.130859'),
(16, 'higher_officer', '0001_initial', '2021-10-12 05:56:56.630859'),
(17, 'higher_officer', '0002_auto_20211012_1246', '2021-10-12 07:25:28.845703'),
(18, 'higher_officer', '0003_station_details_email', '2021-10-12 09:40:08.384765'),
(19, 'higher_officer', '0004_auto_20211021_1234', '2021-10-21 07:04:30.753906'),
(20, 'user', '0002_user_complaints', '2021-10-21 10:59:00.936523'),
(21, 'user', '0003_user_complaints_complaint_status', '2021-10-22 06:37:48.428710'),
(22, 'police', '0001_initial', '2021-10-22 11:16:10.680664');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('hdpi0xmt68xnl8tuud1hkgozn2bmh1p3', 'MzZmM2M2NDNlZTZkNDRmMWY2MGZkNGE2NjZlMWZiOGQ4ZDZmZGNmMzp7InVzZXJpZCI6NCwidXNlcm5hbWUiOiJhcmp1biIsImVtYWlsIjoiY2hlbm5haXN1bmRheXJhbXlhQGdtYWlsLmNvbSIsImFyZWFfY29kZSI6IjAwMSIsInN0YXRpb25fbmFtZSI6IlIzIFBvbGljZSBTdGF0aW9uIn0=', '2021-11-06 09:54:59.388671'),
('zvl8e6w215exik4hudxnb1haghv1re44', 'ZDk0ZWFmY2E1NjgxNTZiNTUyODA2MDEzNWY0ZTBiYTExOTY4NzJlMDp7InVzZXJpZCI6NCwidXNlcm5hbWUiOiI4OTg1NyIsImVtYWlsIjoiY2hlbm5haXN1bmRheXJhbXlhQGdtYWlsLmNvbSJ9', '2021-10-25 13:52:54.785156');

-- --------------------------------------------------------

--
-- Table structure for table `higher_officer_station_details`
--

CREATE TABLE `higher_officer_station_details` (
  `id` int(11) NOT NULL,
  `station_name` varchar(300) NOT NULL,
  `area_code` varchar(200) NOT NULL,
  `location` varchar(200) NOT NULL,
  `gender` varchar(300) NOT NULL,
  `police_name` varchar(300) NOT NULL,
  `email` varchar(200) NOT NULL,
  `area_name` varchar(200) NOT NULL,
  `password` varchar(200) NOT NULL,
  `userid` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `higher_officer_station_details`
--

INSERT INTO `higher_officer_station_details` (`id`, `station_name`, `area_code`, `location`, `gender`, `police_name`, `email`, `area_name`, `password`, `userid`) VALUES
(4, 'R3 Police Station', '001', 'chennai', 'Male', 'arjun', 'chennaisundayramya@gmail.com', 'Ashok Nagar', 'arjun', 'arjun'),
(5, 'R2', '002', 'chennai', 'Male', 'gokul', 'chennaisundayramya@gmail.com', 'west mambalam', 'gokul', 'gokul');

-- --------------------------------------------------------

--
-- Table structure for table `police_criminal_details`
--

CREATE TABLE `police_criminal_details` (
  `id` int(11) NOT NULL,
  `station_name` varchar(300) NOT NULL,
  `arae_code` varchar(200) NOT NULL,
  `city` varchar(200) NOT NULL,
  `criminal_name` varchar(200) NOT NULL,
  `mobile` varchar(200) NOT NULL,
  `complaint_type` varchar(200) NOT NULL,
  `acts` varchar(200) NOT NULL,
  `sessions` varchar(200) NOT NULL,
  `year` varchar(200) NOT NULL,
  `status` varchar(200) NOT NULL,
  `criminal_image` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `police_criminal_details`
--

INSERT INTO `police_criminal_details` (`id`, `station_name`, `arae_code`, `city`, `criminal_name`, `mobile`, `complaint_type`, `acts`, `sessions`, `year`, `status`, `criminal_image`) VALUES
(1, 'R3 Police Station', '001', 'chennai', 'ajay', '9867454545', 'chain snaching', '1992', '23', '2017', 'arrest', 'criminal1.jpg'),
(2, 'R3 Police Station', '001', 'chennai', 'deva', '8967564545', 'Chain snaching', '1992', '23', '2017', 'arrest', 'criminal2.jpg'),
(3, 'R3 Police Station', '001', 'chennai', 'ravi', '5676454545', 'murder', '1992', '23', '2003', 'arrest', 'criminal3.jpg'),
(4, 'R3 Police Station', '001', 'madurai', 'ranjith', '9843123234', 'murder', '1994', '34', '2016', 'arrest', 'criminal4.jpg'),
(5, 'R3 Police Station', '001', 'madurai', 'raman', '9823121212', 'murder', '1993', '34', '2016', 'arrest', 'criminal5.jpg'),
(6, 'R3 Police Station', '001', 'madurai', 'Nandha', '8756454545', 'murder', '1993', '24', '2016', 'arrest', 'criminal6.jpg'),
(7, 'R3 Police Station', '001', 'chennai', 'ragul', '8756454545', 'chain snaching', '1992', '23', '2016', 'arrest', 'criminal7.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `user_user_complaints`
--

CREATE TABLE `user_user_complaints` (
  `id` int(11) NOT NULL,
  `userid` varchar(300) NOT NULL,
  `username` varchar(200) NOT NULL,
  `email` varchar(200) NOT NULL,
  `address` varchar(200) NOT NULL,
  `city` varchar(200) NOT NULL,
  `area_code` varchar(200) NOT NULL,
  `mobile` varchar(200) NOT NULL,
  `date` varchar(200) NOT NULL,
  `complaint_type` varchar(200) NOT NULL,
  `complaint` varchar(200) NOT NULL,
  `complaint_status` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user_user_complaints`
--

INSERT INTO `user_user_complaints` (`id`, `userid`, `username`, `email`, `address`, `city`, `area_code`, `mobile`, `date`, `complaint_type`, `complaint`, `complaint_status`) VALUES
(1, '3', 'ramya', 'chennaisundayramya@gmail.com', '13th street,ashok nagar', 'chennai', '001', '9867565656', '21-10-2021', 'chain snaching', 'my chain is theft by some criminals.', 'Your chain found. Come and collect your chain'),
(2, '5', 'nirmala', 'chennaisundayramya@gmail.com', 'ashok pillar', 'chennai', '001', '9878453434', '23-10-2021', 'chain snaching', 'My chain is theft by some crimibals.', 'Your chain found. Come and collect your chain');

-- --------------------------------------------------------

--
-- Table structure for table `user_user_reg`
--

CREATE TABLE `user_user_reg` (
  `id` int(11) NOT NULL,
  `fullname` varchar(300) NOT NULL,
  `email` varchar(200) NOT NULL,
  `mobile` varchar(200) NOT NULL,
  `gender` varchar(200) NOT NULL,
  `location` varchar(200) NOT NULL,
  `userid` varchar(200) NOT NULL,
  `password` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user_user_reg`
--

INSERT INTO `user_user_reg` (`id`, `fullname`, `email`, `mobile`, `gender`, `location`, `userid`, `password`) VALUES
(3, 'ramya', 'chennaisundayramya@gmail.com', '9876453434', 'Female', 'chennai', 'ramya', 'ramya'),
(4, 'bhuvana', 'chennaisundayramya@gmail.com', '7645344545', 'Female', 'Chennai', '99823', 'i89QB'),
(5, 'nirmala', 'chennaisundayramya@gmail.com', '8767564534', 'Female', 'chennai', 'nirmala', 'nirmala');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `higher_officer_station_details`
--
ALTER TABLE `higher_officer_station_details`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `police_criminal_details`
--
ALTER TABLE `police_criminal_details`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user_user_complaints`
--
ALTER TABLE `user_user_complaints`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user_user_reg`
--
ALTER TABLE `user_user_reg`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT for table `higher_officer_station_details`
--
ALTER TABLE `higher_officer_station_details`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `police_criminal_details`
--
ALTER TABLE `police_criminal_details`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `user_user_complaints`
--
ALTER TABLE `user_user_complaints`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `user_user_reg`
--
ALTER TABLE `user_user_reg`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
