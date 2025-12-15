-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 19, 2025 at 01:52 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `medicweb`
--

-- --------------------------------------------------------

--
-- Table structure for table `appmedic_agendamodel`
--

CREATE TABLE `appmedic_agendamodel` (
  `id` bigint(20) NOT NULL,
  `fecha` date NOT NULL,
  `disponible` tinyint(1) NOT NULL,
  `fk_horario_id` bigint(20) NOT NULL,
  `fk_paciente_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `appmedic_agendamodel`
--

INSERT INTO `appmedic_agendamodel` (`id`, `fecha`, `disponible`, `fk_horario_id`, `fk_paciente_id`) VALUES
(1, '2025-11-25', 0, 1, 1),
(2, '2025-11-26', 0, 9, 2),
(3, '2025-11-27', 0, 15, 3),
(4, '2025-11-28', 0, 2, 4),
(5, '2025-11-29', 0, 12, 5),
(6, '2025-11-25', 0, 5, 6),
(7, '2025-11-26', 0, 6, 1),
(8, '2025-11-27', 0, 16, 2),
(9, '0004-04-05', 1, 2, 1),
(10, '0005-12-05', 1, 11, 7),
(11, '2025-11-13', 1, 9, 8);

-- --------------------------------------------------------

--
-- Table structure for table `appmedic_expedientemodel`
--

CREATE TABLE `appmedic_expedientemodel` (
  `id` bigint(20) NOT NULL,
  `nombre` varchar(15) NOT NULL,
  `descripcion` longtext NOT NULL,
  `fecha_creacion` datetime(6) NOT NULL,
  `fk_paciente_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `appmedic_horariomedicomodel`
--

CREATE TABLE `appmedic_horariomedicomodel` (
  `id` bigint(20) NOT NULL,
  `dia_semana` int(11) NOT NULL,
  `hora_inicio` time(6) NOT NULL,
  `hora_fin` time(6) NOT NULL,
  `activo` tinyint(1) NOT NULL,
  `fk_medico_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `appmedic_horariomedicomodel`
--

INSERT INTO `appmedic_horariomedicomodel` (`id`, `dia_semana`, `hora_inicio`, `hora_fin`, `activo`, `fk_medico_id`) VALUES
(1, 1, '08:00:00.000000', '12:00:00.000000', 1, 6),
(2, 1, '14:00:00.000000', '18:00:00.000000', 1, 6),
(3, 3, '09:00:00.000000', '13:00:00.000000', 1, 6),
(4, 5, '08:00:00.000000', '12:00:00.000000', 1, 6),
(5, 2, '09:00:00.000000', '13:00:00.000000', 1, 7),
(6, 2, '14:00:00.000000', '17:00:00.000000', 1, 7),
(7, 4, '08:30:00.000000', '12:30:00.000000', 1, 7),
(8, 5, '09:00:00.000000', '13:00:00.000000', 1, 7),
(9, 1, '09:30:00.000000', '13:30:00.000000', 1, 8),
(10, 3, '10:00:00.000000', '14:00:00.000000', 1, 8),
(11, 4, '08:00:00.000000', '12:00:00.000000', 1, 8),
(12, 2, '08:00:00.000000', '12:00:00.000000', 1, 9),
(13, 4, '13:00:00.000000', '17:00:00.000000', 1, 9),
(14, 5, '10:00:00.000000', '14:00:00.000000', 1, 9),
(15, 1, '10:00:00.000000', '14:00:00.000000', 1, 10),
(16, 3, '08:00:00.000000', '12:00:00.000000', 1, 10),
(17, 5, '14:00:00.000000', '18:00:00.000000', 1, 10);

-- --------------------------------------------------------

--
-- Table structure for table `appmedic_medicomodel`
--

CREATE TABLE `appmedic_medicomodel` (
  `id` bigint(20) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `correo` varchar(254) NOT NULL,
  `telefono` int(11) NOT NULL,
  `especialidad` varchar(15) NOT NULL,
  `user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `appmedic_medicomodel`
--

INSERT INTO `appmedic_medicomodel` (`id`, `nombre`, `correo`, `telefono`, `especialidad`, `user_id`) VALUES
(6, 'Dr. Carlos González', 'carlos.gonzalez@hospital.cl', 912345678, 'Cardiología', NULL),
(7, 'Dra. María Rodríguez', 'maria.rodriguez@hospital.cl', 923456789, 'Pediatría', NULL),
(8, 'Dr. Juan Martínez', 'juan.martinez@hospital.cl', 934567890, 'Neurología', NULL),
(9, 'Dra. Ana López', 'ana.lopez@hospital.cl', 945678901, 'Dermatología', NULL),
(10, 'Dr. Roberto Fernández', 'roberto.fernandez@hospital.cl', 956789012, 'Oftalmología', NULL),
(11, 'medico3', 'medico3@gmail.com', 123456789, 'rontororinco', NULL),
(12, 'carlos eugenia', 'carlos@gmail.com', 123456789, 'pendejo profesi', NULL),
(13, 'medicoPrueba', 'medicoPrueba@gmail.com', 741852963, 'tango chileno', NULL),
(16, 'Dra. María Pediatra', 'maria@hospital.com', 934567890, 'Pediatría', 49),
(18, 'Dr. Carlos Cardiología', 'carlos@hospital.com', 923456789, 'Cardiología', 50),
(19, 'Dra. María Pediatra', 'maria@hospital.com', 934567890, 'Pediatría', 51),
(20, 'medicoPrueba', 'medicoprueba@gmail.com', 741963852, 'cakecake', NULL),
(21, 'Test Doctor García', 'test@hospital.com', 912345678, 'Neurología', 52),
(22, 'Dra. María López', 'maria@hospital.com', 923456789, 'Pediatría', 53),
(23, 'medicoa', 'medicia@gmail.com', 147852369, 'ropero', 54);

-- --------------------------------------------------------

--
-- Table structure for table `appmedic_pacientemodel`
--

CREATE TABLE `appmedic_pacientemodel` (
  `id` bigint(20) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `rut` varchar(9) NOT NULL,
  `correo` varchar(150) NOT NULL,
  `telefono` int(11) NOT NULL,
  `direccion` varchar(50) NOT NULL,
  `user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `appmedic_pacientemodel`
--

INSERT INTO `appmedic_pacientemodel` (`id`, `nombre`, `rut`, `correo`, `telefono`, `direccion`, `user_id`) VALUES
(1, 'Felipe Sánchez García', '182345679', 'felipe.sanchez@email.com', 987654321, 'Calle Principal 123, Santiago', NULL),
(2, 'Laura Mora Pérez', '193456780', 'laura.mora@email.com', 988765432, 'Avenida Libertad 456, Santiago', NULL),
(3, 'Miguel Torres Guzmán', '174567891', 'miguel.torres@email.com', 989876543, 'Pasaje Central 789, Valparaíso', NULL),
(4, 'Patricia Díaz Vargas', '165678902', 'patricia.diaz@email.com', 990987654, 'Camino al Sur 321, Valparaíso', NULL),
(5, 'Ricardo Navarro Espinoza', '156789013', 'ricardo.navarro@email.com', 991098765, 'Los Acacias 654, Concepción', NULL),
(6, 'Gabriela Herrera Silva', '147890124', 'gabriela.herrera@email.com', 992109876, 'Paseo Real 987, Concepción', NULL),
(7, 'julio cesar', '123456789', 'juliocesar@gmail.com', 123456789, 'direccion generica', NULL),
(8, 'usuario2', '', 'usuario2@gmail.com', 0, '', 45);

-- --------------------------------------------------------

--
-- Table structure for table `appmedic_usuariomodel`
--

CREATE TABLE `appmedic_usuariomodel` (
  `id` bigint(20) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `correo` varchar(254) NOT NULL,
  `usuario` varchar(50) NOT NULL,
  `contraseña` varchar(255) NOT NULL,
  `telefono` varchar(15) NOT NULL,
  `tipo_usuario` varchar(20) NOT NULL,
  `activo` tinyint(1) NOT NULL,
  `fecha_registro` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `appmedic_usuariomodel`
--

INSERT INTO `appmedic_usuariomodel` (`id`, `nombre`, `correo`, `usuario`, `contraseña`, `telefono`, `tipo_usuario`, `activo`, `fecha_registro`) VALUES
(1, 'usuario1', 'usuario@gmail.com', 'usuario1', 'pbkdf2_sha256$600000$FkIGUsHFH9VhFrT6PQL6jk$ZJgxVkWM9FLn3KhLqY49T43nT6mLsFGRxFrrhP3NrCM=', '123456789', 'paciente', 1, '2025-11-18 22:55:33.579974'),
(2, 'admin1', 'admin1@gmail.com', 'admin', 'pbkdf2_sha256$600000$Q0n8ALXcxwn3d8L5K5ZG5h$whmRhiUPLud4iDSyX3i529TVNmnrCUu7AeiI+o79VQw=', '123456789', 'admin', 1, '2025-11-18 23:24:03.210890');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_group`
--

INSERT INTO `auth_group` (`id`, `name`) VALUES
(1, 'Administrador'),
(2, 'Médico'),
(3, 'Paciente');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_group_permissions`
--

INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES
(2, 2, 48),
(3, 2, 52),
(4, 2, 56),
(5, 2, 61),
(6, 2, 62),
(1, 2, 64),
(9, 3, 48),
(8, 3, 56),
(10, 3, 61),
(7, 3, 64);

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add especialidad', 7, 'add_especialidad'),
(26, 'Can change especialidad', 7, 'change_especialidad'),
(27, 'Can delete especialidad', 7, 'delete_especialidad'),
(28, 'Can view especialidad', 7, 'view_especialidad'),
(29, 'Can add medico', 8, 'add_medico'),
(30, 'Can change medico', 8, 'change_medico'),
(31, 'Can delete medico', 8, 'delete_medico'),
(32, 'Can view medico', 8, 'view_medico'),
(33, 'Can add paciente', 9, 'add_paciente'),
(34, 'Can change paciente', 9, 'change_paciente'),
(35, 'Can delete paciente', 9, 'delete_paciente'),
(36, 'Can view paciente', 9, 'view_paciente'),
(37, 'Can add disponibilidad hora', 10, 'add_disponibilidadhora'),
(38, 'Can change disponibilidad hora', 10, 'change_disponibilidadhora'),
(39, 'Can delete disponibilidad hora', 10, 'delete_disponibilidadhora'),
(40, 'Can view disponibilidad hora', 10, 'view_disponibilidadhora'),
(41, 'Can add cita', 11, 'add_cita'),
(42, 'Can change cita', 11, 'change_cita'),
(43, 'Can delete cita', 11, 'delete_cita'),
(44, 'Can view cita', 11, 'view_cita'),
(45, 'Can add medico model', 12, 'add_medicomodel'),
(46, 'Can change medico model', 12, 'change_medicomodel'),
(47, 'Can delete medico model', 12, 'delete_medicomodel'),
(48, 'Can view medico model', 12, 'view_medicomodel'),
(49, 'Can add paciente model', 13, 'add_pacientemodel'),
(50, 'Can change paciente model', 13, 'change_pacientemodel'),
(51, 'Can delete paciente model', 13, 'delete_pacientemodel'),
(52, 'Can view paciente model', 13, 'view_pacientemodel'),
(53, 'Can add Horario Médico', 14, 'add_horariomedicomodel'),
(54, 'Can change Horario Médico', 14, 'change_horariomedicomodel'),
(55, 'Can delete Horario Médico', 14, 'delete_horariomedicomodel'),
(56, 'Can view Horario Médico', 14, 'view_horariomedicomodel'),
(57, 'Can add expediente model', 15, 'add_expedientemodel'),
(58, 'Can change expediente model', 15, 'change_expedientemodel'),
(59, 'Can delete expediente model', 15, 'delete_expedientemodel'),
(60, 'Can view expediente model', 15, 'view_expedientemodel'),
(61, 'Can add agenda model', 16, 'add_agendamodel'),
(62, 'Can change agenda model', 16, 'change_agendamodel'),
(63, 'Can delete agenda model', 16, 'delete_agendamodel'),
(64, 'Can view agenda model', 16, 'view_agendamodel'),
(65, 'Can add Usuario', 17, 'add_usuariomodel'),
(66, 'Can change Usuario', 17, 'change_usuariomodel'),
(67, 'Can delete Usuario', 17, 'delete_usuariomodel'),
(68, 'Can view Usuario', 17, 'view_usuariomodel');

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
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$600000$JbY3X646Co76Wv2IAWEfAC$cr2aR9n8l6dRpSK+TzAs2YR18e1j3fnQMcg+6dN/A04=', '2025-11-19 00:49:25.292666', 1, 'superuser1', '', '', 'superuser1@gmail.com', 1, 1, '2025-11-18 19:51:45.697501'),
(2, 'pbkdf2_sha256$600000$FQg2oJUdnZKRuNVJkuBa6Z$DD8MgpdntdJIIthhe/zsrRCH0TsjsBAh09aaj7dbayg=', '2025-11-19 00:46:04.412724', 1, 'admin', 'Admin', 'Sistema', 'admin@medicsystem.com', 1, 1, '2025-11-18 20:10:39.819171'),
(3, 'pbkdf2_sha256$600000$ieycW4SvXSOUA0YLx1B39P$4+Muemzz+my9x4B03YlUPz4ZlJ82DiFD7yIeC6nm0bY=', '2025-11-19 00:35:48.598087', 0, 'medico1', 'Juan', 'García', 'medico1@medicsystem.com', 0, 1, '2025-11-18 20:10:40.315956'),
(4, 'pbkdf2_sha256$600000$omCvGWh6ZZZmcsoMai3QEi$s4Mup3qbuScjuExIX32u9QfostCBBjWVUjFJGPRKRq4=', NULL, 0, 'medico2', 'María', 'López', 'medico2@medicsystem.com', 0, 1, '2025-11-18 20:10:40.894012'),
(5, 'pbkdf2_sha256$600000$gICYLzMomPzo8b7hzyLI6D$JsS8QLzaggSbmW9IhWDPVPgUCFOzo4vVTJlLAMAkgNc=', NULL, 0, 'medico3', 'Carlos', 'Martínez', 'medico3@medicsystem.com', 0, 1, '2025-11-18 20:10:41.351002'),
(6, 'pbkdf2_sha256$600000$rQ9nVGDMJpedmxajVv7vzQ$lneIQnPz028wo72tpgRAdE8Rg55dBZ/mgfXCN0Bn4/Q=', NULL, 0, 'medico4', 'Ana', 'Rodríguez', 'medico4@medicsystem.com', 0, 1, '2025-11-18 20:10:41.822092'),
(7, 'pbkdf2_sha256$600000$8R33jw5HHPH9Q9avG31B1z$pinrXcAgbCCiXy2zCyjv1wpk3jxPcbszwUwAynQYjWg=', NULL, 0, 'medico5', 'Pedro', 'Sánchez', 'medico5@medicsystem.com', 0, 1, '2025-11-18 20:10:42.314909'),
(8, 'pbkdf2_sha256$600000$42KQ61CVEoneXRQexnTuR0$eJLF7i901mrm9Vycf6Y61grq5omHs9kF26pc7cDrLDQ=', NULL, 0, 'medico6', 'Laura', 'González', 'medico6@medicsystem.com', 0, 1, '2025-11-18 20:10:42.776705'),
(9, 'pbkdf2_sha256$600000$WKSqEjBo1qvZOlRLT0ionn$y57gmW2ahwksY2we5kG5TxVN8BqFlgUxmz1fTDQPrdM=', NULL, 0, 'medico7', 'Roberto', 'Pérez', 'medico7@medicsystem.com', 0, 1, '2025-11-18 20:10:43.240514'),
(10, 'pbkdf2_sha256$600000$9PPvDD9pgr84STfqnpBqbL$btJHtOGDYgZ60KKHBw9k4ahBdUBLkGw1s6AxTgLRwO4=', NULL, 0, 'medico8', 'Sofia', 'Ramírez', 'medico8@medicsystem.com', 0, 1, '2025-11-18 20:10:43.717996'),
(11, 'pbkdf2_sha256$600000$dESP0wGoV30qzPG8lok2Xu$ljNPf/9wM+Vub9yAhjBBZ623S3G6waciCe1+KDFRiBo=', NULL, 0, 'medico9', 'Miguel', 'Torres', 'medico9@medicsystem.com', 0, 1, '2025-11-18 20:10:44.313473'),
(12, 'pbkdf2_sha256$600000$9qRbahvBLTXE9ZJ6gXdSBZ$o77IPUnf7PxZ4P87JVbnCwakuhBWQZPlgF5aCPAkjZQ=', NULL, 0, 'medico10', 'Isabel', 'Rivera', 'medico10@medicsystem.com', 0, 1, '2025-11-18 20:10:44.884208'),
(13, 'pbkdf2_sha256$600000$qFBRUaARcuHoPiERY14KYI$ieU8rZ6guhC3+9MDHRKleOEBCRP/0sDdXTmz2JpTUu8=', NULL, 0, 'medico11', 'Luis', 'Cruz', 'medico11@medicsystem.com', 0, 1, '2025-11-18 20:10:45.380224'),
(14, 'pbkdf2_sha256$600000$xcWkvOWvVC2h0C8lidpujn$3N5ICKZZHibGNUQ31Jcnw2Sr7XqIjRBWdyDoafZmCXQ=', NULL, 0, 'medico12', 'Rosa', 'Flores', 'medico12@medicsystem.com', 0, 1, '2025-11-18 20:10:45.914007'),
(15, 'pbkdf2_sha256$600000$tfO104Ata1Kq1NrfevPmLK$HH4MQ4hfG6Qazvb/BbAexNyuMHjLzeITc4Mo+lTLoT4=', NULL, 0, 'medico13', 'Antonio', 'Morales', 'medico13@medicsystem.com', 0, 1, '2025-11-18 20:10:46.468376'),
(16, 'pbkdf2_sha256$600000$BzX9UVxvyNVgk8QWdLpdxJ$7EKPIHvunlvWC+qcuZyri+mW5BEqiRhXAETG9AgcsEQ=', NULL, 0, 'medico14', 'Carmen', 'Vargas', 'medico14@medicsystem.com', 0, 1, '2025-11-18 20:10:46.997472'),
(17, 'pbkdf2_sha256$600000$izL51846BHTnnQVXxl5j3Y$edC0ughPEUB+7Z4gglpA+5h4RtTN3MYvMhTUgT5QSTA=', NULL, 0, 'medico15', 'Francisco', 'Medina', 'medico15@medicsystem.com', 0, 1, '2025-11-18 20:10:47.535268'),
(18, 'pbkdf2_sha256$600000$3PRgi7xSUDi6iEwmMIPNJn$0uACS9qanXF2M0VV5g5jTJEA97Dkxox35hINNVz8sm8=', NULL, 0, 'paciente1', 'Diego', 'Acosta', 'paciente1@medicsystem.com', 0, 1, '2025-11-18 20:10:48.031058'),
(19, 'pbkdf2_sha256$600000$NOW7VN13Du7zXWQYE3BfPP$sZKR/SthfyFciekp6US7qemdeOKu3NkRZMhZpF8lNWA=', NULL, 0, 'paciente2', 'Emma', 'Bravo', 'paciente2@medicsystem.com', 0, 1, '2025-11-18 20:10:48.617781'),
(20, 'pbkdf2_sha256$600000$4w4uVidNxQWKqcX8Ucxoo3$yjW8Zr3MMUKzpxWmGGwkPQCOruICoEelP/946foq7Pg=', NULL, 0, 'paciente3', 'Andrés', 'Cabrera', 'paciente3@medicsystem.com', 0, 1, '2025-11-18 20:10:49.230540'),
(21, 'pbkdf2_sha256$600000$W2c9HJp1AZB1x9zPUSb1Up$gl3uZajGmnZrSEjrg2E1tsZNs5xaL9DIy2IwzI4o2TE=', NULL, 0, 'paciente4', 'Valeria', 'Díaz', 'paciente4@medicsystem.com', 0, 1, '2025-11-18 20:10:49.745401'),
(22, 'pbkdf2_sha256$600000$YFmGOpIGZU4mV4mqgsLo2K$YWj7j/kjd4S3XZBpAGkRpkaj14+4k1t4IwS581pm7Jc=', NULL, 0, 'paciente5', 'Pablo', 'Espinoza', 'paciente5@medicsystem.com', 0, 1, '2025-11-18 20:10:50.328744'),
(23, 'pbkdf2_sha256$600000$N9HaxOSrmPV2bGlwEyS7FD$sSqUrRBUh4XBmDhJmYv09ELuQNKv4I2+VaR5PkoORCo=', NULL, 0, 'paciente6', 'Marcela', 'Fuentes', 'paciente6@medicsystem.com', 0, 1, '2025-11-18 20:10:50.834306'),
(24, 'pbkdf2_sha256$600000$uKo26EDA7rjME4UanchIDP$SZaHR0GQk3GGzCjIWqwDgsxg3TrhJl6ixLs1cZdF3GU=', NULL, 0, 'paciente7', 'Javier', 'Gómez', 'paciente7@medicsystem.com', 0, 1, '2025-11-18 20:10:51.364246'),
(25, 'pbkdf2_sha256$600000$FaWFKywP4osOym256h5ipA$zOVa0JEh30v1XJbFuzZqzY5XykO0nfagD4mmc0E65zI=', NULL, 0, 'paciente8', 'Daniela', 'Herrera', 'paciente8@medicsystem.com', 0, 1, '2025-11-18 20:10:51.964226'),
(26, 'pbkdf2_sha256$600000$G8bZqkuAdEt6lVBZYFxnFY$A1LBD/XcTSWhGczqC3LbUgFN4bn9VTAhRuAtgoPLRwk=', NULL, 0, 'paciente9', 'Ricardo', 'Iglesias', 'paciente9@medicsystem.com', 0, 1, '2025-11-18 20:10:52.489111'),
(27, 'pbkdf2_sha256$600000$POhyvtr7de3KCwB7acf6Rx$OSoGia65gRsZkLqyka5k5iHcyY2cLZywH+nr/HO/5cE=', NULL, 0, 'paciente10', 'Alejandra', 'Jiménez', 'paciente10@medicsystem.com', 0, 1, '2025-11-18 20:10:53.011639'),
(28, 'pbkdf2_sha256$600000$OhtGMapHUXoQq2FyeWKnyN$W7ldee6nMm1UlRohQOoLkoSAO6cIF1bFgtfVvC9rtHk=', NULL, 0, 'paciente11', 'Fernando', 'Keller', 'paciente11@medicsystem.com', 0, 1, '2025-11-18 20:10:53.492533'),
(29, 'pbkdf2_sha256$600000$LqXJccqOMBKWGLfpLnhxSb$a/auHbhu1HrCaZA8DirL0fAIINXxtn4pI8mkA+TIYNQ=', NULL, 0, 'paciente12', 'Beatriz', 'Lara', 'paciente12@medicsystem.com', 0, 1, '2025-11-18 20:10:53.889797'),
(30, 'pbkdf2_sha256$600000$fqJFciD8tzWCRDpaIbl6Ly$Eh906AAC3UnB50fB/yzcGxUkVbPuyNrbz2DViI1o37A=', NULL, 0, 'paciente13', 'Sergio', 'Mendez', 'paciente13@medicsystem.com', 0, 1, '2025-11-18 20:10:54.482608'),
(31, 'pbkdf2_sha256$600000$Nb29yd2xSvNWsBLLKndggX$1RP9ORpcBg+Bahrqh9AQ7NYPMnQ6KQh9+EKMMXngwso=', NULL, 0, 'paciente14', 'Patricia', 'Nava', 'paciente14@medicsystem.com', 0, 1, '2025-11-18 20:10:54.999566'),
(32, 'pbkdf2_sha256$600000$NBO8WNFtsLnl0Dwaq4lHbv$zFr2sKdT0wQa+7zT4UmhsZmnk89OAwPBpRy6wCV1XGw=', NULL, 0, 'paciente15', 'Gustavo', 'Ortega', 'paciente15@medicsystem.com', 0, 1, '2025-11-18 20:10:55.499008'),
(33, 'pbkdf2_sha256$600000$FVvo8DQM1CYsgK4ekmXCJd$CEvUoYG6Rodg44Qk+VKTPrSqF35XYwXK7IgPZ0xPvrE=', NULL, 0, 'paciente16', 'Mónica', 'Pacheco', 'paciente16@medicsystem.com', 0, 1, '2025-11-18 20:10:55.988572'),
(34, 'pbkdf2_sha256$600000$kV0Uur61Xc7AjA6d5b6A50$Oqbgcifo5CFUVsYXz/xX44PnwfbFAQ63PtxVV5ETJCc=', NULL, 0, 'paciente17', 'Eduardo', 'Quintero', 'paciente17@medicsystem.com', 0, 1, '2025-11-18 20:10:56.472267'),
(35, 'pbkdf2_sha256$600000$ACy3qTW4CCb7mLZid0UUc9$xhTsNTZKOJhGiNizJFzBqD34+3objs7rulZH1AWYOBk=', NULL, 0, 'paciente18', 'Silvia', 'Reyes', 'paciente18@medicsystem.com', 0, 1, '2025-11-18 20:10:56.960345'),
(36, 'pbkdf2_sha256$600000$YPagZdVtT2K0gEexUmOv5h$Dj1gEC0rxcy84HRRrjHHS4P92nXMgLuM6fAswy8eqrE=', NULL, 0, 'paciente19', 'Álvaro', 'Soto', 'paciente19@medicsystem.com', 0, 1, '2025-11-18 20:10:57.452318'),
(37, 'pbkdf2_sha256$600000$UcKJHWNm6ddcEt5zVhqpo9$bR6m3HR9jn3O6D1jB45BBMr4fxhbvMzC3cKk3tWS0+w=', NULL, 0, 'paciente20', 'Teresa', 'Uriarte', 'paciente20@medicsystem.com', 0, 1, '2025-11-18 20:10:57.915850'),
(38, 'pbkdf2_sha256$600000$4CjuTL1uVakO1xCoYMkOog$dUhcqcvzx8QQ0/aL/fGActbab0WCARnBoMmLF9T/bZY=', NULL, 0, 'paciente21', 'Ramón', 'Valencia', 'paciente21@medicsystem.com', 0, 1, '2025-11-18 20:10:58.417965'),
(39, 'pbkdf2_sha256$600000$HOlY6ZaI0WiqhahyfyfCEE$+dBxMfoa+ItXe/YNvRDlA6tEhQqeTTWNrHoKyYtRBXY=', NULL, 0, 'paciente22', 'Verónica', 'Walters', 'paciente22@medicsystem.com', 0, 1, '2025-11-18 20:10:58.907288'),
(40, 'pbkdf2_sha256$600000$B8aFxpCGOZQMO9tzYlJVDl$2l9EZsTjT+4/sFZy/54u4j0fn0jePZZYrNPPDtewQps=', NULL, 0, 'paciente23', 'Vicente', 'Xerez', 'paciente23@medicsystem.com', 0, 1, '2025-11-18 20:10:59.461308'),
(41, 'pbkdf2_sha256$600000$qcFvzfz0nTch5adcZAtGDo$KLEx3ymBgjh5rYBt0avS3m3HdFSeDUb9z5YiXbakjtA=', NULL, 0, 'paciente24', 'Ximena', 'Yáñez', 'paciente24@medicsystem.com', 0, 1, '2025-11-18 20:11:00.026277'),
(42, 'pbkdf2_sha256$600000$uUrx4G9KbEjlFw4YFudbsW$aZEggaGCkzcd3h2jA9X5lRC5fX0LKqTkvIpKGThFWjo=', NULL, 0, 'paciente25', 'Zoraida', 'Zambrano', 'paciente25@medicsystem.com', 0, 1, '2025-11-18 20:11:00.528230'),
(43, 'pbkdf2_sha256$600000$3BGtvWO5PzDVeI3ifdtdod$2VS4q3s1K1KzQzM+JSsNA7AQ4eahCZuZnI9FA/g5VZk=', NULL, 1, '12345678', '', '', 'superuser1@gmail.com', 1, 1, '2025-11-18 23:22:29.268586'),
(44, 'pbkdf2_sha256$600000$o4wqIJJs42iVkma6oGyjl5$FXzxhPuT4tuPkjY3t4FXfK9QqcwuOdXHaUyWpWRI2sM=', '2025-11-19 00:10:28.202527', 0, 'usuario1', 'usuario', '', 'usuario1@gmail.com', 0, 1, '2025-11-18 23:41:20.510524'),
(45, 'pbkdf2_sha256$600000$fHjlSCHW6hThexFO3CGEMW$TRIdDQjYZ2of+Svnm2R8g698790E4CAyWPniBS822EA=', '2025-11-18 23:54:38.035346', 0, 'usuario2', 'usuario2', '', 'usuario2@gmail.com', 0, 1, '2025-11-18 23:54:31.929296'),
(49, 'pbkdf2_sha256$600000$R9PrrxAdHiAlhv3sMShp38$4rvtoyEpLukuL8iV164iL1yjwfS6q185RnVrfg1UV8E=', NULL, 0, 'dra._maría_pediatra', 'Dra. María Pediatra', '', 'maria@hospital.com', 0, 1, '2025-11-19 00:38:20.397955'),
(50, 'pbkdf2_sha256$600000$Rslyv7QI5Gknw5FUmPWAEr$P9ukOvIM9QIAEGr+QF/eKcvsbkZveSxRvwOmKJNleaE=', NULL, 0, 'dr_cardiologo', 'Dr. Carlos Cardiología', '', 'carlos@hospital.com', 0, 1, '2025-11-19 00:38:48.426336'),
(51, 'pbkdf2_sha256$600000$uOzfjyh5gSDnmnIgFNJTyV$rSl4ppjaZOByDy3D1Q9A03Ougk2jRi2xtVnv0WzDDB8=', NULL, 0, 'dra_maria_pediatra', 'Dra. María Pediatra', '', 'maria@hospital.com', 0, 1, '2025-11-19 00:38:49.418570'),
(52, 'pbkdf2_sha256$600000$G2qu9d1CtYfZYOk7Ra8qeX$ls1fvItFLON8elhCbB/4VLL+LPzQZnncwLw9/QvDWCs=', NULL, 0, 'test_doctor_garcia', 'Test Doctor García', '', 'test@hospital.com', 0, 1, '2025-11-19 00:46:02.434697'),
(53, 'pbkdf2_sha256$600000$26W4J9tgRBmKDkOtBdBm5g$0QfieZkfm6cfAZyzLAcTZAtjKFYxhIcqIJD5q4Fqkcc=', NULL, 0, 'dra_maria_lopez', 'Dra. María López', '', 'maria@hospital.com', 0, 1, '2025-11-19 00:46:03.378321'),
(54, 'pbkdf2_sha256$600000$XBy4K9TEa6sMK44OSId7RW$4HRnna051cuCUPnG972MVUY3DxK0SMFs6d15w5rMijQ=', '2025-11-19 00:49:10.561119', 0, 'adivino', 'medicoa', '', 'medicia@gmail.com', 0, 1, '2025-11-19 00:48:31.570543');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_user_groups`
--

INSERT INTO `auth_user_groups` (`id`, `user_id`, `group_id`) VALUES
(1, 2, 1),
(2, 3, 2),
(3, 4, 2),
(4, 5, 2),
(5, 6, 2),
(6, 7, 2),
(7, 8, 2),
(8, 9, 2),
(9, 10, 2),
(10, 11, 2),
(11, 12, 2),
(12, 13, 2),
(13, 14, 2),
(14, 15, 2),
(15, 16, 2),
(16, 17, 2),
(17, 18, 3),
(18, 19, 3),
(19, 20, 3),
(20, 21, 3),
(21, 22, 3),
(22, 23, 3),
(23, 24, 3),
(24, 25, 3),
(25, 26, 3),
(26, 27, 3),
(27, 28, 3),
(28, 29, 3),
(29, 30, 3),
(30, 31, 3),
(31, 32, 3),
(32, 33, 3),
(33, 34, 3),
(34, 35, 3),
(35, 36, 3),
(36, 37, 3),
(37, 38, 3),
(38, 39, 3),
(39, 40, 3),
(40, 41, 3),
(41, 42, 3),
(42, 44, 3),
(43, 45, 3),
(47, 49, 2),
(48, 50, 2),
(49, 51, 2),
(50, 52, 2),
(51, 53, 2),
(52, 54, 2);

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `cita`
--

CREATE TABLE `cita` (
  `id_cita` int(11) NOT NULL,
  `fecha_cita` date NOT NULL,
  `hora_cita` time(6) NOT NULL,
  `motivo` longtext NOT NULL,
  `estado` varchar(20) NOT NULL,
  `notas_medico` longtext NOT NULL,
  `fecha_creacion` datetime(6) NOT NULL,
  `fecha_actualizacion` datetime(6) NOT NULL,
  `id_medico_id` int(11) NOT NULL,
  `id_paciente_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `disponibilidad_hora`
--

CREATE TABLE `disponibilidad_hora` (
  `id_disponibilidad` int(11) NOT NULL,
  `dia_semana` varchar(20) NOT NULL,
  `hora_inicio` time(6) NOT NULL,
  `hora_fin` time(6) NOT NULL,
  `duracion_cita` int(11) NOT NULL,
  `id_medico_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `disponibilidad_hora`
--

INSERT INTO `disponibilidad_hora` (`id_disponibilidad`, `dia_semana`, `hora_inicio`, `hora_fin`, `duracion_cita`, `id_medico_id`) VALUES
(1, 'MON', '08:00:00.000000', '17:00:00.000000', 30, 1),
(2, 'MON', '09:00:00.000000', '17:00:00.000000', 30, 1),
(3, 'TUE', '09:00:00.000000', '17:00:00.000000', 30, 2),
(4, 'TUE', '10:00:00.000000', '17:00:00.000000', 30, 2),
(5, 'TUE', '14:00:00.000000', '17:00:00.000000', 30, 2),
(6, 'WED', '10:00:00.000000', '17:00:00.000000', 30, 3),
(7, 'WED', '14:00:00.000000', '17:00:00.000000', 30, 3),
(8, 'THU', '14:00:00.000000', '17:00:00.000000', 30, 4),
(9, 'THU', '15:00:00.000000', '17:00:00.000000', 30, 4),
(10, 'THU', '08:00:00.000000', '17:00:00.000000', 30, 4),
(11, 'FRI', '15:00:00.000000', '17:00:00.000000', 30, 5),
(12, 'FRI', '08:00:00.000000', '17:00:00.000000', 30, 5),
(13, 'MON', '08:00:00.000000', '17:00:00.000000', 30, 6),
(14, 'MON', '09:00:00.000000', '17:00:00.000000', 30, 6),
(15, 'MON', '10:00:00.000000', '17:00:00.000000', 30, 6),
(16, 'TUE', '09:00:00.000000', '17:00:00.000000', 30, 7),
(17, 'TUE', '10:00:00.000000', '17:00:00.000000', 30, 7),
(18, 'WED', '10:00:00.000000', '17:00:00.000000', 30, 8),
(19, 'WED', '14:00:00.000000', '17:00:00.000000', 30, 8),
(20, 'WED', '15:00:00.000000', '17:00:00.000000', 30, 8),
(21, 'THU', '14:00:00.000000', '17:00:00.000000', 30, 9),
(22, 'THU', '15:00:00.000000', '17:00:00.000000', 30, 9),
(23, 'FRI', '15:00:00.000000', '17:00:00.000000', 30, 10),
(24, 'FRI', '08:00:00.000000', '17:00:00.000000', 30, 10),
(25, 'FRI', '09:00:00.000000', '17:00:00.000000', 30, 10),
(26, 'MON', '08:00:00.000000', '17:00:00.000000', 30, 11),
(27, 'MON', '09:00:00.000000', '17:00:00.000000', 30, 11),
(28, 'TUE', '09:00:00.000000', '17:00:00.000000', 30, 12),
(29, 'TUE', '10:00:00.000000', '17:00:00.000000', 30, 12),
(30, 'TUE', '14:00:00.000000', '17:00:00.000000', 30, 12),
(31, 'WED', '10:00:00.000000', '17:00:00.000000', 30, 13),
(32, 'WED', '14:00:00.000000', '17:00:00.000000', 30, 13),
(33, 'THU', '14:00:00.000000', '17:00:00.000000', 30, 14),
(34, 'THU', '15:00:00.000000', '17:00:00.000000', 30, 14),
(35, 'THU', '08:00:00.000000', '17:00:00.000000', 30, 14),
(36, 'FRI', '15:00:00.000000', '17:00:00.000000', 30, 15),
(37, 'FRI', '08:00:00.000000', '17:00:00.000000', 30, 15);

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(16, 'appMedic', 'agendamodel'),
(11, 'appMedic', 'cita'),
(10, 'appMedic', 'disponibilidadhora'),
(7, 'appMedic', 'especialidad'),
(15, 'appMedic', 'expedientemodel'),
(14, 'appMedic', 'horariomedicomodel'),
(8, 'appMedic', 'medico'),
(12, 'appMedic', 'medicomodel'),
(9, 'appMedic', 'paciente'),
(13, 'appMedic', 'pacientemodel'),
(17, 'appMedic', 'usuariomodel'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2025-11-18 19:49:48.190523'),
(2, 'auth', '0001_initial', '2025-11-18 19:49:48.659948'),
(3, 'admin', '0001_initial', '2025-11-18 19:49:48.761056'),
(4, 'admin', '0002_logentry_remove_auto_add', '2025-11-18 19:49:48.769869'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2025-11-18 19:49:48.778685'),
(7, 'appMedic', '0002_alter_paciente_numero_cedula', '2025-11-18 19:49:49.189819'),
(8, 'contenttypes', '0002_remove_content_type_name', '2025-11-18 19:49:49.246304'),
(9, 'auth', '0002_alter_permission_name_max_length', '2025-11-18 19:49:49.296850'),
(10, 'auth', '0003_alter_user_email_max_length', '2025-11-18 19:49:49.310317'),
(11, 'auth', '0004_alter_user_username_opts', '2025-11-18 19:49:49.320436'),
(12, 'auth', '0005_alter_user_last_login_null', '2025-11-18 19:49:49.359013'),
(13, 'auth', '0006_require_contenttypes_0002', '2025-11-18 19:49:49.361847'),
(14, 'auth', '0007_alter_validators_add_error_messages', '2025-11-18 19:49:49.371806'),
(15, 'auth', '0008_alter_user_username_max_length', '2025-11-18 19:49:49.385549'),
(16, 'auth', '0009_alter_user_last_name_max_length', '2025-11-18 19:49:49.399800'),
(17, 'auth', '0010_alter_group_name_max_length', '2025-11-18 19:49:49.415999'),
(18, 'auth', '0011_update_proxy_permissions', '2025-11-18 19:49:49.428837'),
(19, 'auth', '0012_alter_user_first_name_max_length', '2025-11-18 19:49:49.444443'),
(20, 'sessions', '0001_initial', '2025-11-18 19:49:49.469332'),
(21, 'appMedic', '0002_add_fields', '2025-11-18 22:01:36.950587'),
(22, 'appMedic', '0001_initial', '2025-11-18 22:10:40.512836'),
(23, 'appMedic', '0002_usuariomodel', '2025-11-18 22:26:53.635083'),
(24, 'appMedic', '0003_pacientemodel_user', '2025-11-18 23:44:25.399690'),
(25, 'appMedic', '0004_medicomodel_user', '2025-11-18 23:59:24.258955');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('0naj5s3pv36vpilr6j1ilq281ey6mj3v', '.eJxVjDsOwyAQRO9CHSEQsLAp0-cMiOUTnERYMnZl5e4xkotkynlvZmc-bGv1W8-LnxK7Mm3Z5bekEF-5DZKeoT1mHue2LhPxofCTdn6fU37fTvfvoIZej7UgkC7qFBDJaWsIXEQFsmB2QTuhDGIBUUxGUgCplKGQdVIcyZZ9vvm3N3I:1vLW1r:LlE_2Uf20Qwf7QN16krQBnVvwtTfaABq6eQdGkAXeSM', '2025-12-03 00:26:35.407978'),
('518f6kj5hfx5cecyjdkv1qhbhpjiqtef', '.eJxVjDsOwjAQRO_iGlnrjdfGlPScwVr_cAA5UpxUiLuTSCmgnHlv5i08r0v1a8-zH5O4CBSn3y5wfOa2g_Tgdp9knNoyj0Huijxol7cp5df1cP8OKve6rTWSM4UyaygwJLRbBAgOSKMNASk6c1ZFqYBJR02WFcScI4MBsoMRny-3nDbP:1vLW2D:wTsLrihPngSGQBVUMJ_yQghGkhLy826-m7N2lMj1mdI', '2025-12-03 00:26:57.540978'),
('6u8ay10xb16c1n5cxbgc5fm0qbtt5p8e', '.eJxVjDsOwjAQRO_iGlnrjdfGlPScwVr_cAA5UpxUiLuTSCmgnHlv5i08r0v1a8-zH5O4CBSn3y5wfOa2g_Tgdp9knNoyj0Huijxol7cp5df1cP8OKve6rTWSM4UyaygwJLRbBAgOSKMNASk6c1ZFqYBJR02WFcScI4MBsoMRny-3nDbP:1vLW6T:oNnJg7fJa3YxaQbIWhreRD6HTiUcy57fTMnQLkL69Zg', '2025-12-03 00:31:21.561811'),
('83fb0g8p09iwnmwgh9em6za2rz6k27d7', '.eJxVjDsOwjAQRO_iGlnrjdfGlPScwVr_cAA5UpxUiLuTSCmgnHlv5i08r0v1a8-zH5O4CBSn3y5wfOa2g_Tgdp9knNoyj0Huijxol7cp5df1cP8OKve6rTWSM4UyaygwJLRbBAgOSKMNASk6c1ZFqYBJR02WFcScI4MBsoMRny-3nDbP:1vLVu9:UB7R_ybxvvQZe_krq-sKqKqI1O9hY4BSrOnJ9hzAJZk', '2025-12-03 00:18:37.053504'),
('lipzeavuy0277rwxfislz0woun08mgu1', '.eJxVjDsOwjAQRO_iGlnrjdfGlPScwVr_cAA5UpxUiLuTSCmgnHlv5i08r0v1a8-zH5O4CBSn3y5wfOa2g_Tgdp9knNoyj0Huijxol7cp5df1cP8OKve6rTWSM4UyaygwJLRbBAgOSKMNASk6c1ZFqYBJR02WFcScI4MBsoMRny-3nDbP:1vLVuU:KBLtHzzn6no9NvgIQS49KDCg6GCp_Si4SVMX68VUc-g', '2025-12-03 00:18:58.871040'),
('malzbczxfizr4rm6o1f1447qbc4urcd2', '.eJxVjMsOwiAQRf-FtSFAeY1L934DAYaRqoGktCvjv2uTLnR7zzn3xULc1hq2UZYwIzszyU6_W4r5UdoO8B7brfPc27rMie8KP-jg147leTncv4MaR_3WWmonShQTGS8TIORkJZCi7JGMtclogEkIlJPNQKisc6Clj0TaKu_Z-wPReTc0:1vLWNx:hF0nE9j_uUD46xo4nQ7lewngYqIT7W-ak4E69T-M7Wc', '2025-12-03 00:49:25.295147'),
('scduts9sc97y13qw24bu3um7adfg3csj', '.eJxVjDsOwjAQRO_iGlnrjdfGlPScwVr_cAA5UpxUiLuTSCmgnHlv5i08r0v1a8-zH5O4CBSn3y5wfOa2g_Tgdp9knNoyj0Huijxol7cp5df1cP8OKve6rTWSM4UyaygwJLRbBAgOSKMNASk6c1ZFqYBJR02WFcScI4MBsoMRny-3nDbP:1vLW69:J5xFfC0VZWU0tB3wMH-lgMnmj5IA71pN4IaHUzD4J2M', '2025-12-03 00:31:01.214143'),
('ud72lvaedttv2l2ed66mhaz2qknyj8yc', '.eJxVjDsOwjAQRO_iGlnrjdfGlPScwVr_cAA5UpxUiLuTSCmgnHlv5i08r0v1a8-zH5O4CBSn3y5wfOa2g_Tgdp9knNoyj0Huijxol7cp5df1cP8OKve6rTWSM4UyaygwJLRbBAgOSKMNASk6c1ZFqYBJR02WFcScI4MBsoMRny-3nDbP:1vLWKi:L38oqLHbeFPiCCelDOMaBxeWQrkc3psfNkld5eI3gDU', '2025-12-03 00:46:04.414299');

-- --------------------------------------------------------

--
-- Table structure for table `especialidad`
--

CREATE TABLE `especialidad` (
  `id_especialidad` int(11) NOT NULL,
  `nombre` varchar(200) NOT NULL,
  `descripcion` longtext DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `especialidad`
--

INSERT INTO `especialidad` (`id_especialidad`, `nombre`, `descripcion`) VALUES
(1, 'Cardiología', NULL),
(2, 'Dermatología', NULL),
(3, 'Ginecología', NULL),
(4, 'Neurología', NULL),
(5, 'Oftalmología', NULL),
(6, 'Otorrinolaringología', NULL),
(7, 'Pediatría', NULL),
(8, 'Psiquiatría', NULL),
(9, 'Traumatología', NULL),
(10, 'Urología', NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `appmedic_agendamodel`
--
ALTER TABLE `appmedic_agendamodel`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `appMedic_agendamodel_fk_horario_id_fecha_87b98e13_uniq` (`fk_horario_id`,`fecha`),
  ADD KEY `appMedic_agendamodel_fk_paciente_id_01c4d94b_fk_appMedic_` (`fk_paciente_id`);

--
-- Indexes for table `appmedic_expedientemodel`
--
ALTER TABLE `appmedic_expedientemodel`
  ADD PRIMARY KEY (`id`),
  ADD KEY `appMedic_expedientem_fk_paciente_id_45f8302b_fk_appMedic_` (`fk_paciente_id`);

--
-- Indexes for table `appmedic_horariomedicomodel`
--
ALTER TABLE `appmedic_horariomedicomodel`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `appMedic_horariomedicomo_fk_medico_id_dia_semana__7a8b06ea_uniq` (`fk_medico_id`,`dia_semana`,`hora_inicio`);

--
-- Indexes for table `appmedic_medicomodel`
--
ALTER TABLE `appmedic_medicomodel`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Indexes for table `appmedic_pacientemodel`
--
ALTER TABLE `appmedic_pacientemodel`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Indexes for table `appmedic_usuariomodel`
--
ALTER TABLE `appmedic_usuariomodel`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `correo` (`correo`),
  ADD UNIQUE KEY `usuario` (`usuario`);

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
-- Indexes for table `cita`
--
ALTER TABLE `cita`
  ADD PRIMARY KEY (`id_cita`),
  ADD UNIQUE KEY `cita_id_medico_id_fecha_cita_hora_cita_0c4fe3a0_uniq` (`id_medico_id`,`fecha_cita`,`hora_cita`),
  ADD KEY `cita_id_paciente_id_a841f5fb_fk_paciente_id_paciente` (`id_paciente_id`);

--
-- Indexes for table `disponibilidad_hora`
--
ALTER TABLE `disponibilidad_hora`
  ADD PRIMARY KEY (`id_disponibilidad`),
  ADD UNIQUE KEY `disponibilidad_hora_id_medico_id_dia_semana__504bb2b5_uniq` (`id_medico_id`,`dia_semana`,`hora_inicio`,`hora_fin`);

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
-- Indexes for table `especialidad`
--
ALTER TABLE `especialidad`
  ADD PRIMARY KEY (`id_especialidad`),
  ADD UNIQUE KEY `nombre` (`nombre`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `appmedic_agendamodel`
--
ALTER TABLE `appmedic_agendamodel`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `appmedic_expedientemodel`
--
ALTER TABLE `appmedic_expedientemodel`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `appmedic_horariomedicomodel`
--
ALTER TABLE `appmedic_horariomedicomodel`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `appmedic_medicomodel`
--
ALTER TABLE `appmedic_medicomodel`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `appmedic_pacientemodel`
--
ALTER TABLE `appmedic_pacientemodel`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `appmedic_usuariomodel`
--
ALTER TABLE `appmedic_usuariomodel`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=69;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=55;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=53;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `cita`
--
ALTER TABLE `cita`
  MODIFY `id_cita` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `disponibilidad_hora`
--
ALTER TABLE `disponibilidad_hora`
  MODIFY `id_disponibilidad` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=38;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `especialidad`
--
ALTER TABLE `especialidad`
  MODIFY `id_especialidad` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `appmedic_agendamodel`
--
ALTER TABLE `appmedic_agendamodel`
  ADD CONSTRAINT `appMedic_agendamodel_fk_horario_id_9b3405a3_fk_appMedic_` FOREIGN KEY (`fk_horario_id`) REFERENCES `appmedic_horariomedicomodel` (`id`),
  ADD CONSTRAINT `appMedic_agendamodel_fk_paciente_id_01c4d94b_fk_appMedic_` FOREIGN KEY (`fk_paciente_id`) REFERENCES `appmedic_pacientemodel` (`id`);

--
-- Constraints for table `appmedic_expedientemodel`
--
ALTER TABLE `appmedic_expedientemodel`
  ADD CONSTRAINT `appMedic_expedientem_fk_paciente_id_45f8302b_fk_appMedic_` FOREIGN KEY (`fk_paciente_id`) REFERENCES `appmedic_pacientemodel` (`id`);

--
-- Constraints for table `appmedic_horariomedicomodel`
--
ALTER TABLE `appmedic_horariomedicomodel`
  ADD CONSTRAINT `appMedic_horariomedi_fk_medico_id_92a32a8b_fk_appMedic_` FOREIGN KEY (`fk_medico_id`) REFERENCES `appmedic_medicomodel` (`id`);

--
-- Constraints for table `appmedic_medicomodel`
--
ALTER TABLE `appmedic_medicomodel`
  ADD CONSTRAINT `appMedic_medicomodel_user_id_a1ebbf78_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `appmedic_pacientemodel`
--
ALTER TABLE `appmedic_pacientemodel`
  ADD CONSTRAINT `appMedic_pacientemodel_user_id_87d5e77a_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

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
-- Constraints for table `cita`
--
ALTER TABLE `cita`
  ADD CONSTRAINT `cita_id_medico_id_3a1bfdeb_fk_medico_id_medico` FOREIGN KEY (`id_medico_id`) REFERENCES `medico` (`id_medico`),
  ADD CONSTRAINT `cita_id_paciente_id_a841f5fb_fk_paciente_id_paciente` FOREIGN KEY (`id_paciente_id`) REFERENCES `paciente` (`id_paciente`);

--
-- Constraints for table `disponibilidad_hora`
--
ALTER TABLE `disponibilidad_hora`
  ADD CONSTRAINT `disponibilidad_hora_id_medico_id_f3949c5e_fk_medico_id_medico` FOREIGN KEY (`id_medico_id`) REFERENCES `medico` (`id_medico`);

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
