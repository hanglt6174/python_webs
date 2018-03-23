CREATE TABLE IF NOT EXISTS `user` (
  `user_id` int(8) NOT NULL AUTO_INCREMENT,
  `user_username` varchar(64) NOT NULL,
  `user_pass` varchar(64) NOT NULL,
  `user_role` char(1) NOT NULL DEFAULT 0,
  `user_email` varchar(64) NOT NULL,
  `user_fullname` varchar(64) NOT NULL,
  `user_nickname` varchar(64) NOT NULL,
  `user_postcode` int(7) NOT NULL,
  `user_address` varchar(128) NOT NULL,
  `user_tel` varchar(12) NOT NULL,
  `user_datecreated` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `user_creator` int(8) NOT NULL,
  `user_dateupdated` datetime NOT NULL,
  `user_updater` int(8) NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;