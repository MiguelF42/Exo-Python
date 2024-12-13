DROP TABLE IF EXISTS `users_etudiant`;
CREATE TABLE `users_etudiant`(
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `login` VARCHAR(32) NOT NULL,
    `password` VARCHAR(1024) NOT NULL,
    `fname` VARCHAR(255) NOT NULL,
    `lname` VARCHAR(255) NOT NULL,
    `nb_etudiant` VARCHAR(255) NOT NULL,
    `specialite` VARCHAR(255) NOT NULL,
    `is_admin` BOOLEAN NOT NULL,
    `ban_date` DATETIME
)