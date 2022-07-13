-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema bgda_db
-- -----------------------------------------------------
-- This database schema is for the Bluegrass Darting Association (BGDA)

-- -----------------------------------------------------
-- Schema bgda_db
--
-- This database schema is for the Bluegrass Darting Association (BGDA)
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `bgda_db` DEFAULT CHARACTER SET utf8 ;
USE `bgda_db` ;

-- -----------------------------------------------------
-- Table `bgda_db`.`players`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bgda_db`.`players` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(25) NOT NULL,
  `last_name` VARCHAR(25) NOT NULL,
  `phone_number` VARCHAR(10) NULL,
  `email` VARCHAR(50) NULL,
  `nickname` VARCHAR(25) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `bgda_db`.`seasons`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bgda_db`.`seasons` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(10) NOT NULL,
  `year` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `bgda_db`.`bars`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bgda_db`.`bars` (
  `name` VARCHAR(45) NOT NULL,
  `address` VARCHAR(45) NOT NULL,
  `id` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `bgda_db`.`teams`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bgda_db`.`teams` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `home_bar_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `home_bar_id_idx` (`home_bar_id` ASC) VISIBLE,
  CONSTRAINT `teams_home_bar`
    FOREIGN KEY (`home_bar_id`)
    REFERENCES `bgda_db`.`bars` (`id`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `bgda_db`.`divisions`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bgda_db`.`divisions` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `bgda_db`.`fixtures`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bgda_db`.`fixtures` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `season_id` INT NOT NULL,
  `division_id` INT NOT NULL,
  `home_team_id` INT NOT NULL,
  `away_team_id` INT NOT NULL,
  `winning_team_id` INT NOT NULL,
  `losing_team_id` INT NOT NULL,
  `match_date` DATE NOT NULL,
  `home_team_score` INT NOT NULL,
  `away_team_score` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `season_idx` (`season_id` ASC) VISIBLE,
  INDEX `division_idx` (`division_id` ASC) VISIBLE,
  INDEX `home_team_idx` (`home_team_id` ASC) VISIBLE,
  INDEX `away_team_idx` (`away_team_id` ASC) VISIBLE,
  INDEX `winning_team_idx` (`winning_team_id` ASC) VISIBLE,
  INDEX `losing_team_idx` (`losing_team_id` ASC) VISIBLE,
  CONSTRAINT `fixtures_season`
    FOREIGN KEY (`season_id`)
    REFERENCES `bgda_db`.`seasons` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fixtures_division`
    FOREIGN KEY (`division_id`)
    REFERENCES `bgda_db`.`divisions` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fixtures_home_team`
    FOREIGN KEY (`home_team_id`)
    REFERENCES `bgda_db`.`teams` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fixtures_away_team`
    FOREIGN KEY (`away_team_id`)
    REFERENCES `bgda_db`.`teams` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fixtures_winning_team`
    FOREIGN KEY (`winning_team_id`)
    REFERENCES `bgda_db`.`teams` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fixtures_losing_team`
    FOREIGN KEY (`losing_team_id`)
    REFERENCES `bgda_db`.`teams` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `bgda_db`.`rosters`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bgda_db`.`rosters` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `season_id` INT NOT NULL,
  `division_id` INT NOT NULL,
  `team_id` INT NOT NULL,
  `player_id` INT NOT NULL,
  `player_is_captain` TINYINT(1) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `season_idx` (`season_id` ASC) VISIBLE,
  INDEX `division_idx` (`division_id` ASC) VISIBLE,
  INDEX `team_idx` (`team_id` ASC) VISIBLE,
  INDEX `player_idx` (`player_id` ASC) VISIBLE,
  CONSTRAINT `rosters_season`
    FOREIGN KEY (`season_id`)
    REFERENCES `bgda_db`.`seasons` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `rosters_division`
    FOREIGN KEY (`division_id`)
    REFERENCES `bgda_db`.`divisions` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `rosters_team`
    FOREIGN KEY (`team_id`)
    REFERENCES `bgda_db`.`teams` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `rosters_player`
    FOREIGN KEY (`player_id`)
    REFERENCES `bgda_db`.`players` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `bgda_db`.`registrations`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bgda_db`.`registrations` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `game_date` DATE NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
COMMENT = 'This table is part of the solution to being able to differentiate between singles and doubles games.';


-- -----------------------------------------------------
-- Table `bgda_db`.`scoresheets`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bgda_db`.`scoresheets` (
  `registration_id` INT NOT NULL,
  `player_roster_id` INT NOT NULL,
  INDEX `registration_idx` (`registration_id` ASC) VISIBLE,
  INDEX `player_idx` (`player_roster_id` ASC) VISIBLE,
  CONSTRAINT `scoresheets_registration`
    FOREIGN KEY (`registration_id`)
    REFERENCES `bgda_db`.`registrations` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `scoresheets_player`
    FOREIGN KEY (`player_roster_id`)
    REFERENCES `bgda_db`.`rosters` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `bgda_db`.`games`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bgda_db`.`games` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL COMMENT '501 SIDO / Cricket / 401 DIDO / etc.',
  `category` VARCHAR(45) NOT NULL COMMENT 'Singles / doubles / etc.',
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `bgda_db`.`fixtures_details`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bgda_db`.`fixtures_details` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `fixure_id` INT NOT NULL,
  `game_id` INT NOT NULL,
  `home_registration_id` INT NOT NULL,
  `away_registration_id` INT NOT NULL,
  `home_registration_score` INT ZEROFILL NOT NULL,
  `away_registration_score` INT ZEROFILL NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fixture_idx` (`fixure_id` ASC) VISIBLE,
  INDEX `game_idx` (`game_id` ASC) VISIBLE,
  INDEX `home_registration_idx` (`home_registration_id` ASC) VISIBLE,
  INDEX `away_registration_idx` (`away_registration_id` ASC) VISIBLE,
  CONSTRAINT `fixture_details_fixture`
    FOREIGN KEY (`fixure_id`)
    REFERENCES `bgda_db`.`fixtures` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fixture_details_game`
    FOREIGN KEY (`game_id`)
    REFERENCES `bgda_db`.`games` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fixture_details_home_registration`
    FOREIGN KEY (`home_registration_id`)
    REFERENCES `bgda_db`.`registrations` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fixture_details_away_registration`
    FOREIGN KEY (`away_registration_id`)
    REFERENCES `bgda_db`.`registrations` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `bgda_db`.`awards`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bgda_db`.`awards` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `inagural_date` DATE NULL,
  `description` VARCHAR(250) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `bgda_db`.`players_awards`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bgda_db`.`players_awards` (
  `award_id` INT NOT NULL,
  `player_roster_id` INT NOT NULL,
  INDEX `award_idx` (`award_id` ASC) VISIBLE,
  INDEX `player_idx` (`player_roster_id` ASC) VISIBLE,
  CONSTRAINT `player_awards_award`
    FOREIGN KEY (`award_id`)
    REFERENCES `bgda_db`.`awards` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `player_awards_player`
    FOREIGN KEY (`player_roster_id`)
    REFERENCES `bgda_db`.`rosters` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `bgda_db`.`awards_tracking`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bgda_db`.`awards_tracking` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `fixture_id` INT NOT NULL,
  `player_roster_id` INT NOT NULL,
  `award_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fixture_idx` (`fixture_id` ASC) VISIBLE,
  INDEX `player_idx` (`player_roster_id` ASC) VISIBLE,
  INDEX `award_idx` (`award_id` ASC) VISIBLE,
  CONSTRAINT `awards_tracking_fixture`
    FOREIGN KEY (`fixture_id`)
    REFERENCES `bgda_db`.`fixtures` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `awards_tracking_player`
    FOREIGN KEY (`player_roster_id`)
    REFERENCES `bgda_db`.`rosters` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `awards_tracking_award`
    FOREIGN KEY (`award_id`)
    REFERENCES `bgda_db`.`awards` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
