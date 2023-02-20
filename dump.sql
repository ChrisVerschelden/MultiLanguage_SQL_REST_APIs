CREATE TABLE IF NOT EXISTS customers (
  id int(11) NOT NULL,
  firstname varchar(200) NOT NULL,
  name varchar(200) NOT NULL,
  email varchar(200) NOT NULL,
  created datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

ALTER TABLE users ADD PRIMARY KEY (id);
ALTER TABLE users MODIFY id int(11) NOT NULL AUTO_INCREMENT;

INSERT INTO `customers` (`id`, `firstname`, `name`, `email`, `created`) VALUES
  (1, 'John','Doe', 'johndoe@gmail.com', '2012-06-01 02:12:30'),
  (2, 'David','Costa', 'dav.costa1548@yahoo.com', '2013-03-03 01:20:10'),
  (3, 'Todd','Martell', 'tood.m4975@gmail.com', '2014-09-20 03:10:25'),
  (4, 'Adela','Marion', 'madela2004@yahoo.com', '2015-04-11 04:11:12'),
  (5, 'Matthew','Popp', 'matcorn@gmail.com', '2016-01-04 05:20:30'),
  (6, 'Alan','Wallin', 'alan-wall@hotmail.com', '2017-01-10 06:40:10'),
  (7, 'Joyce','Hinze', 'hjoyce27@yahoo.com', '2017-05-02 02:20:30'),
  (8, 'Donna','Andrews', 'andrews179584@yahoo.com', '2018-01-04 05:15:35'),
  (9, 'Andrew','Best', 'andrew.best24@hotmail.com', '2019-01-02 02:20:30'),
  (10, 'Joel','Ogle', 'joel.ogle245987@hotmail.com', '2020-02-01 06:22:50');