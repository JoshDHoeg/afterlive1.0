-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`Family`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Family` (
  `Family_ID` INT NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(256) NOT NULL,
  PRIMARY KEY (`Family_ID`),
  UNIQUE INDEX `FamilyID_UNIQUE` (`Family_ID` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Identity`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Identity` (
  `Identity_ID` INT NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(256) NOT NULL,
  PRIMARY KEY (`Identity_ID`),
  UNIQUE INDEX `idIdentity_UNIQUE` (`Identity_ID` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Genre`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Genre` (
  `Genre_ID` INT NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(256) NOT NULL,
  PRIMARY KEY (`Genre_ID`),
  UNIQUE INDEX `idGenre_UNIQUE` (`Genre_ID` ASC))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `mydb`.`Link`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Link` (
  `LinkID` INT NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(256) NOT NULL,
  `Facebook` VARCHAR(256) NULL,
  `Instagram` VARCHAR(256) NULL,
  `Youtube` VARCHAR(256) NULL,
  `Twitter` VARCHAR(256) NULL,
  `Spotify` VARCHAR(256) NULL,
  `Soundcloud` VARCHAR(256) NULL,
  `Tumblr` VARCHAR(256) NULL,
  `Website` VARCHAR(256) NULL,
  PRIMARY KEY (`LinkID`),
  UNIQUE INDEX `Linke_ID_UNIQUE` (`LinkID` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Account`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Account` (
  `account_id` INT NOT NULL AUTO_INCREMENT,
  `Username` VARCHAR(256) NULL,
  `Password` VARCHAR(256) NULL,
  `Email` VARCHAR(256) NULL,
  `Background` LONGBLOB NULL,
  `Profile` LONGBLOB NULL,
  `Bio` TEXT NULL,
  `Account_Link_ID` INT NULL,
  PRIMARY KEY (`account_id`),
  UNIQUE INDEX `idAccount_UNIQUE` (`account_id` ASC),
  UNIQUE INDEX `Username_UNIQUE` (`Username` ASC),
  INDEX `fk_Account_Link1_idx` (`Account_Link_ID` ASC),
  CONSTRAINT `fk_Account_Link1`
    FOREIGN KEY (`Account_Link_ID`)
    REFERENCES `mydb`.`Link` (`LinkID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Country`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Country` (
  `Country_ID` INT NOT NULL AUTO_INCREMENT,
  `country_code` varchar(2) NOT NULL default '',
  `Country_Name` VARCHAR(256) NOT NULL default '',
  PRIMARY KEY (`Country_ID`),
  UNIQUE INDEX `Country_ID_UNIQUE` (`Country_ID` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`User`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`User` (
  `User_ID` INT NOT NULL AUTO_INCREMENT,
  `First_Name` VARCHAR(256) NULL,
  `Last_Name` VARCHAR(256) NULL,
  `Gender` ENUM('male', 'female', 'other') NULL,
  `User_Family_ID` INT NULL,
  `User_Identity_ID` INT NULL,
  `User_Account_ID` INT NULL,
  `User_Country_ID` INT NULL,
  PRIMARY KEY (`User_ID`),
  UNIQUE INDEX `User_ID_UNIQUE` (`User_ID` ASC),
  INDEX `fk_User_Family1_idx` (`User_Family_ID` ASC),
  INDEX `fk_User_Identity1_idx` (`User_Identity_ID` ASC),
  INDEX `fk_User_Account1_idx` (`User_Account_ID` ASC),
  INDEX `fk_User_Country1_idx` (`User_Country_ID` ASC),
  CONSTRAINT `fk_User_Family1`
    FOREIGN KEY (`User_Family_ID`)
    REFERENCES `mydb`.`Family` (`Family_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_User_Identity1`
    FOREIGN KEY (`User_Identity_ID`)
    REFERENCES `mydb`.`Identity` (`Identity_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_User_Account1`
    FOREIGN KEY (`User_Account_ID`)
    REFERENCES `mydb`.`Account` (`account_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_User_Country1`
    FOREIGN KEY (`User_Country_ID`)
    REFERENCES `mydb`.`Country` (`Country_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Festival`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Festival` (
  `Festival_ID` INT NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(256) NULL,
  `Start_Date` DATE NULL,
  `End_Date` DATE NULL,
  `Festival_Account_id` INT NULL,
  `Festival_Venue_id` INT NULL,
  PRIMARY KEY (`Festival_ID`),
  UNIQUE INDEX `idFestival_UNIQUE` (`Festival_ID` ASC),
  INDEX `fk_Festival_Account1_idx` (`Festival_Account_id` ASC),
  INDEX `fk_Festival_Venue1_idx` (`Festival_Venue_id` ASC),
  CONSTRAINT `fk_Festival_Account1`
    FOREIGN KEY (`Festival_Account_id`)
    REFERENCES `mydb`.`Account` (`account_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Festival_Venue1`
    FOREIGN KEY (`Festival_Venue_id`)
    REFERENCES `mydb`.`Venue` (`Venue_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Artist`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Artist` (
  `Artist_ID` INT NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(256) NULL,
  `City` VARCHAR(256) NULL,
  `Artist_Genre_ID` INT NULL,
  `Artist_Identity_ID` INT NULL,
  `Artist_Account_ID` INT NULL,
  `Artist_Country_ID` INT NULL,
  `Artist_Family_ID` INT NULL,
  PRIMARY KEY (`Artist_ID`),
  UNIQUE INDEX `idArtist_UNIQUE` (`Artist_ID` ASC),
  INDEX `fk_Artist_Genre1_idx` (`Artist_Genre_ID` ASC),
  INDEX `fk_Artist_Identity1_idx` (`Artist_Identity_ID` ASC),
  INDEX `fk_Artist_Account1_idx` (`Artist_Account_ID` ASC),
  INDEX `fk_Artist_Country1_idx` (`Artist_Country_ID` ASC),
  INDEX `fk_Artist_Family1_idx` (`Artist_Family_ID` ASC),
  CONSTRAINT `fk_Artist_Genre1`
    FOREIGN KEY (`Artist_Genre_ID`)
    REFERENCES `mydb`.`Genre` (`Genre_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Artist_Identity1`
    FOREIGN KEY (`Artist_Identity_ID`)
    REFERENCES `mydb`.`Identity` (`Identity_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Artist_Account1`
    FOREIGN KEY (`Artist_Account_ID`)
    REFERENCES `mydb`.`Account` (`account_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Artist_Country1`
    FOREIGN KEY (`Artist_Country_ID`)
    REFERENCES `mydb`.`Country` (`Country_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Artist_Family1`
    FOREIGN KEY (`Artist_Family_ID`)
    REFERENCES `mydb`.`Family` (`Family_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Festival Follower`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Festival_Follower` (
  `Festival_User_ID` INT NOT NULL AUTO_INCREMENT,
  `F_ID` INT NOT NULL,
  `U_ID` INT NOT NULL,
  PRIMARY KEY (`Festival_User_ID`),
  INDEX `fk_Festival_has_User_User1_idx` (`U_ID` ASC),
  INDEX `fk_Festival_has_User_Festival_idx` (`F_ID` ASC),
  UNIQUE INDEX `FU_ID_UNIQUE` (`Festival_User_ID` ASC),
  CONSTRAINT `fk_Festival_has_User_Festival`
    FOREIGN KEY (`F_ID`)
    REFERENCES `mydb`.`Festival` (`Festival_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Festival_has_User_User1`
    FOREIGN KEY (`U_ID`)
    REFERENCES `mydb`.`User` (`User_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Artist Follower`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Artist_Follower` (
  `U_ID` INT NOT NULL,
  `A_ID` INT NOT NULL,
  `Artist_User_ID` INT NOT NULL AUTO_INCREMENT,
  INDEX `fk_User_has_Artist_Artist1_idx` (`A_ID` ASC),
  INDEX `fk_User_has_Artist_User1_idx` (`U_ID` ASC),
  PRIMARY KEY (`Artist_User_ID`),
  UNIQUE INDEX `Artist_User_Connectioncol_UNIQUE` (`Artist_User_ID` ASC),
  CONSTRAINT `fk_User_has_Artist_User1`
    FOREIGN KEY (`U_ID`)
    REFERENCES `mydb`.`User` (`User_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_User_has_Artist_Artist1`
    FOREIGN KEY (`A_ID`)
    REFERENCES `mydb`.`Artist` (`Artist_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Venue`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Venue` (
  `Venue_ID` INT NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(256) NULL,
  `City` VARCHAR(256) NULL,
  `Venue_State_ID` INT NULL,
  `Venue_Country_ID` INT NULL,
  PRIMARY KEY (`Venue_ID`),
  UNIQUE INDEX `idVenue_UNIQUE` (`Venue_ID` ASC),
  INDEX `fk_Venue_Country1_idx` (`Venue_Country_ID` ASC),
  INDEX `fk_Venue_State1_idx` (`Venue_State_ID` ASC),
  CONSTRAINT `fk_State_State1`
    FOREIGN KEY (`Venue_State_ID`)
    REFERENCES `mydb`.`State` (`State_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Venue_Country1`
    FOREIGN KEY (`Venue_Country_ID`)
    REFERENCES `mydb`.`Country` (`Country_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Photographer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Photographer` (
  `Photographer_ID` INT NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(256) NULL,
  `First_Name` VARCHAR(256) NULL,
  `Last_Name` VARCHAR(256) NULL,
  `Gender` ENUM('female', 'male', 'other') NULL,
  `Photographer_Family_ID` INT NULL,
  `Photographer_Identity_ID` INT NULL,
  `Photographer_Account_ID` INT NULL,
  `Photographer_Country_ID` INT NULL,
  PRIMARY KEY (`Photographer_ID`),
  UNIQUE INDEX `Photographer_ID_UNIQUE` (`Photographer_ID` ASC),
  INDEX `fk_Photographer_Family1_idx` (`Photographer_Family_ID` ASC),
  INDEX `fk_Photographer_Identity1_idx` (`Photographer_Identity_ID` ASC),
  INDEX `fk_Photographer_Account1_idx` (`Photographer_Account_ID` ASC),
  INDEX `fk_Photographer_Country1_idx` (`Photographer_Country_ID` ASC),
  CONSTRAINT `fk_Photographer_Family1`
    FOREIGN KEY (`Photographer_Family_ID`)
    REFERENCES `mydb`.`Family` (`Family_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Photographer_Identity1`
    FOREIGN KEY (`Photographer_Identity_ID`)
    REFERENCES `mydb`.`Identity` (`Identity_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Photographer_Account1`
    FOREIGN KEY (`Photographer_Account_ID`)
    REFERENCES `mydb`.`Account` (`account_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Photographer_Country1`
    FOREIGN KEY (`Photographer_Country_ID`)
    REFERENCES `mydb`.`Country` (`Country_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Festival_has_Photographer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Festival_has_Photographer` (
  `Festival_Festival_ID` INT NOT NULL,
  `Photographer_Photographer_ID` INT NOT NULL,
  `Photographer_Festival_ID` INT NOT NULL,
  PRIMARY KEY (`Photographer_Festival_ID`),
  INDEX `fk_Festival_has_Photographer_Photographer1_idx` (`Photographer_Photographer_ID` ASC),
  INDEX `fk_Festival_has_Photographer_Festival1_idx` (`Festival_Festival_ID` ASC),
  CONSTRAINT `fk_Festival_has_Photographer_Festival1`
    FOREIGN KEY (`Festival_Festival_ID`)
    REFERENCES `mydb`.`Festival` (`Festival_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Festival_has_Photographer_Photographer1`
    FOREIGN KEY (`Photographer_Photographer_ID`)
    REFERENCES `mydb`.`Photographer` (`Photographer_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Festival_Artist`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Festival_Artist` (
  `Fl_ID` INT NOT NULL,
  `A_ID` INT NOT NULL,
  `Festival_Artist_ID` INT NOT NULL AUTO_INCREMENT,
  INDEX `fk_Festival_has_Artist_Artist1_idx` (`A_ID` ASC),
  INDEX `fk_Festival_has_Artist_Festival1_idx` (`Fl_ID` ASC),
  PRIMARY KEY (`Festival_Artist_ID`),
  UNIQUE INDEX `FA_ID_UNIQUE` (`Festival_Artist_ID` ASC),
  CONSTRAINT `fk_Festival_has_Artist_Festival1`
    FOREIGN KEY (`Fl_ID`)
    REFERENCES `mydb`.`Festival` (`Festival_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Festival_has_Artist_Artist1`
    FOREIGN KEY (`A_ID`)
    REFERENCES `mydb`.`Artist` (`Artist_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Photographer_Artist`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Photographer_Artist` (
  `P_ID` INT NOT NULL,
  `A_ID` INT NOT NULL,
  `Photographer_Artist_ID` INT NOT NULL AUTO_INCREMENT,
  INDEX `fk_Photographer_has_Artist_Artist1_idx` (`A_ID` ASC),
  INDEX `fk_Photographer_has_Artist_Photographer1_idx` (`P_ID` ASC),
  PRIMARY KEY (`Photographer_Artist_ID`),
  UNIQUE INDEX `PA_ID_UNIQUE` (`Photographer_Artist_ID` ASC),
  CONSTRAINT `fk_Photographer_has_Artist_Photographer1`
    FOREIGN KEY (`P_ID`)
    REFERENCES `mydb`.`Photographer` (`Photographer_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Photographer_has_Artist_Artist1`
    FOREIGN KEY (`A_ID`)
    REFERENCES `mydb`.`Artist` (`Artist_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Photographer Follower`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Photographer_Follower` (
  `U_ID` INT NOT NULL,
  `P_ID` INT NOT NULL,
  `UP_ID` INT NOT NULL AUTO_INCREMENT,
  INDEX `fk_User_has_Photographer_Photographer1_idx` (`P_ID` ASC),
  INDEX `fk_User_has_Photographer_User1_idx` (`U_ID` ASC),
  PRIMARY KEY (`UP_ID`),
  UNIQUE INDEX `UP_ID_UNIQUE` (`UP_ID` ASC),
  CONSTRAINT `fk_User_has_Photographer_User1`
    FOREIGN KEY (`U_ID`)
    REFERENCES `mydb`.`User` (`User_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_User_has_Photographer_Photographer1`
    FOREIGN KEY (`P_ID`)
    REFERENCES `mydb`.`Photographer` (`Photographer_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Culture`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Culture` (
  `Culture_ID` INT NOT NULL AUTO_INCREMENT,
  `Tag` VARCHAR(256) NOT NULL,
  PRIMARY KEY (`Culture_ID`),
  UNIQUE INDEX `idCulture_UNIQUE` (`Culture_ID` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Type`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Type` (
  `Type_ID` INT NOT NULL AUTO_INCREMENT,
  `Content_Type` VARCHAR(256) NOT NULL,
  PRIMARY KEY (`Type_ID`),
  UNIQUE INDEX `idType_UNIQUE` (`Type_ID` ASC))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `mydb`.`State`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`State` (
  `State_ID` INT NOT NULL AUTO_INCREMENT,
  `State` VARCHAR(256) NOT NULL,
  `State_code` varchar(2) NOT NULL default '',
  PRIMARY KEY (`State_ID`),
  UNIQUE INDEX `idState_UNIQUE` (`State_ID` ASC))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `mydb`.`Content`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Content` (
  `Content_ID` INT NOT NULL AUTO_INCREMENT,
  `Account` VARCHAR(256) NOT NULL,
  `Origin` ENUM('Youtube', 'Instagram') NOT NULL,
  `Content_Value` TEXT NOT NULL,
  `Content_Photographer_ID` INT NULL,
  `Content_User_ID` INT NULL,
  `Content_Artist_ID` INT NULL,
  `Content_Festival_ID` INT NULL,
  `Content_Culture_ID` INT NULL,
  `Content_Type_ID` INT NULL,
  PRIMARY KEY (`Content_ID`),
  UNIQUE INDEX `idContent_UNIQUE` (`Content_ID` ASC),
  INDEX `fk_Content_Photographer1_idx` (`Content_Photographer_ID` ASC),
  INDEX `fk_Content_User1_idx` (`Content_User_ID` ASC),
  INDEX `fk_Content_Artist1_idx` (`Content_Artist_ID` ASC),
  INDEX `fk_Content_Festival1_idx` (`Content_Festival_ID` ASC),
  INDEX `fk_Content_Culture1_idx` (`Content_Culture_ID` ASC),
  INDEX `fk_Content_Type1_idx` (`Content_Type_ID` ASC),
  CONSTRAINT `fk_Content_Photographer1`
    FOREIGN KEY (`Content_Photographer_ID`)
    REFERENCES `mydb`.`Photographer` (`Photographer_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Content_User1`
    FOREIGN KEY (`Content_User_ID`)
    REFERENCES `mydb`.`User` (`User_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Content_Artist1`
    FOREIGN KEY (`Content_Artist_ID`)
    REFERENCES `mydb`.`Artist` (`Artist_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Content_Festival1`
    FOREIGN KEY (`Content_Festival_ID`)
    REFERENCES `mydb`.`Festival` (`Festival_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Content_Culture1`
    FOREIGN KEY (`Content_Culture_ID`)
    REFERENCES `mydb`.`Culture` (`Culture_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Content_Type1`
    FOREIGN KEY (`Content_Type_ID`)
    REFERENCES `mydb`.`Type` (`Type_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`User Playlists`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`User_Playlists` (
  `PlaylistID` INT NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(256) NOT NULL,
  `Playlist_User_ID` INT NOT NULL,
  PRIMARY KEY (`PlaylistID`),
  UNIQUE INDEX `PlaylistsID_UNIQUE` (`PlaylistID` ASC),
  INDEX `fk_User Playlists_User1_idx` (`Playlist_User_ID` ASC),
  CONSTRAINT `fk_User Playlists_User1`
    FOREIGN KEY (`Playlist_User_ID`)
    REFERENCES `mydb`.`User` (`User_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`User Playlists_has_User`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`User Playlists_has_User` (
  `User Playlists_PlaylistsID` INT NOT NULL,
  `User_User_ID` INT NOT NULL,
  PRIMARY KEY (`User Playlists_PlaylistsID`, `User_User_ID`),
  INDEX `fk_User Playlists_has_User_User1_idx` (`User_User_ID` ASC),
  INDEX `fk_User Playlists_has_User_User Playlists1_idx` (`User Playlists_PlaylistsID` ASC),
  CONSTRAINT `fk_User Playlists_has_User_User Playlists1`
    FOREIGN KEY (`User Playlists_PlaylistsID`)
    REFERENCES `mydb`.`User Playlists` (`PlaylistID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_User Playlists_has_User_User1`
    FOREIGN KEY (`User_User_ID`)
    REFERENCES `mydb`.`User` (`User_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Playlist Content`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `mydb`.`Playlist_Content` (
  `Playlist_p_ID` INT NOT NULL,
  `Playlist_c_ID` INT NOT NULL,
  PRIMARY KEY (`Playlist_p_ID`, `Playlist_c_ID`),
  INDEX `fk_User Playlists_has_Content_Content1_idx` (`Playlist_c_ID` ASC),
  INDEX `fk_User Playlists_has_Content_User Playlists1_idx` (`Playlist_p_ID` ASC),
  CONSTRAINT `fk_User Playlists_has_Content_User Playlists1`
    FOREIGN KEY (`Playlist_p_ID`)
    REFERENCES `mydb`.`User Playlists` (`PlaylistID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_User Playlists_has_Content_Content1`
    FOREIGN KEY (`Playlist_c_ID`)
    REFERENCES `mydb`.`Content` (`Content_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Likes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Likes` (
  `Content_Content_ID` INT NOT NULL,
  `User_User_ID` INT NOT NULL,
  PRIMARY KEY (`Content_Content_ID`, `User_User_ID`),
  INDEX `fk_Content_has_User_User1_idx` (`User_User_ID` ASC),
  INDEX `fk_Content_has_User_Content1_idx` (`Content_Content_ID` ASC),
  CONSTRAINT `fk_Content_has_User_Content1`
    FOREIGN KEY (`Content_Content_ID`)
    REFERENCES `mydb`.`Content` (`Content_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Content_has_User_User1`
    FOREIGN KEY (`User_User_ID`)
    REFERENCES `mydb`.`User` (`User_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;



SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
