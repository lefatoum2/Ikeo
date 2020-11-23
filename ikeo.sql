-- phpMyAdmin SQL Dump
-- version 4.9.5
-- https://www.phpmyadmin.net/
--
-- Hôte : localhost:8081
-- Généré le : ven. 20 nov. 2020 à 12:58
-- Version du serveur :  5.7.24
-- Version de PHP : 7.4.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `ikeo`
--
CREATE DATABASE IF NOT EXISTS `ikeo` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `ikeo`;

-- --------------------------------------------------------

--
-- Structure de la table `clients`
--

CREATE TABLE `clients` (
  `id_client` int(11) NOT NULL,
  `id_type` int(11) NOT NULL,
  `id_raison` int(11) NOT NULL,
  `adresse_client` varchar(50) NOT NULL,
  `id_ville` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `clients`
--

INSERT INTO `clients` (`id_client`, `id_type`, `id_raison`, `adresse_client`, `id_ville`) VALUES
(1, 1, 1, 'Place Vendôme', 4),
(2, 1, 2, 'Porte de Brandebourg', 5),
(3, 1, 1, 'Rue Jean Jaurès', 6),
(4, 1, 3, 'Rue de la Bastille', 4),
(5, 1, 1, 'Avenue des trois dragons', 7),
(6, 2, 4, 'Oxford street', 8),
(7, 1, 5, 'Coven Garden', 8);

-- --------------------------------------------------------

--
-- Structure de la table `facture`
--

CREATE TABLE `facture` (
  `id_facture` int(11) NOT NULL,
  `numero_facture` varchar(70) NOT NULL,
  `date_facture` date NOT NULL,
  `id_client` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `facture`
--

INSERT INTO `facture` (`id_facture`, `numero_facture`, `date_facture`, `id_client`) VALUES
(1, 'MSQ291', '2018-06-15', 1),
(2, 'MSQ292', '2018-06-23', 5),
(3, 'MSQ293', '2018-06-23', 6),
(4, 'MSQ294', '2018-06-28', 1),
(5, 'MSQ295', '2018-07-01', 4),
(6, 'MSQ296', '2018-07-04', 7),
(7, 'MSQ297', '2018-07-12', 2);

-- --------------------------------------------------------

--
-- Structure de la table `factures_produit`
--

CREATE TABLE `factures_produit` (
  `id_facture` int(11) NOT NULL,
  `id_produit` int(11) NOT NULL,
  `quantite` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `factures_produit`
--

INSERT INTO `factures_produit` (`id_facture`, `id_produit`, `quantite`) VALUES
(1, 1, 20),
(4, 1, 10),
(5, 1, 25),
(1, 2, 30),
(4, 2, 10),
(6, 2, 40),
(1, 3, 10),
(3, 3, 80),
(2, 4, 32),
(3, 4, 60),
(7, 4, 20),
(3, 5, 70),
(6, 5, 38),
(7, 5, 34),
(3, 6, 60),
(4, 6, 30),
(6, 6, 54),
(7, 6, 45),
(2, 7, 25),
(3, 8, 120),
(3, 9, 90),
(5, 9, 34);

-- --------------------------------------------------------

--
-- Structure de la table `produits`
--

CREATE TABLE `produits` (
  `id_produit` int(11) NOT NULL,
  `nom_produit` varchar(50) NOT NULL,
  `ref_produit` varchar(50) NOT NULL,
  `aband_produit` tinyint(1) NOT NULL,
  `desription_produit` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `produits`
--

INSERT INTO `produits` (`id_produit`, `nom_produit`, `ref_produit`, `aband_produit`, `desription_produit`) VALUES
(1, 'Knutsen', 'OANT72', 0, 'Table basse pour poser les bières'),
(2, 'Moen', 'OANT34', 1, 'Chaise haute de bar'),
(3, 'Eide', 'OANT67', 0, 'Porte-serviettes pour 100 serviettes'),
(4, 'Gulbrandsen', 'LXAL34', 0, 'Lit nuage en levitation'),
(5, 'Naess', 'LXAL56', 0, 'Table 128 convives'),
(6, 'Lund', 'LXAL78', 1, 'Tiroir à rond de serviette'),
(7, 'Ruud', 'OANT90', 0, 'Bureau-lit conbiné'),
(8, 'Apfelguck', 'OANT12', 0, 'Panier à chien ou chat'),
(9, 'Dahl', 'LXAL12', 1, 'Tiroir à rond de serviette');

-- --------------------------------------------------------

--
-- Structure de la table `produit_site`
--

CREATE TABLE `produit_site` (
  `id_site` int(11) NOT NULL,
  `id_produit` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `produit_site`
--

INSERT INTO `produit_site` (`id_site`, `id_produit`) VALUES
(1, 1),
(2, 1),
(1, 2),
(2, 2),
(1, 3),
(3, 3),
(3, 4),
(1, 5),
(3, 5),
(2, 5),
(1, 6),
(3, 6),
(2, 9),
(3, 9),
(3, 7),
(3, 8);

-- --------------------------------------------------------

--
-- Structure de la table `raison_sociale`
--

CREATE TABLE `raison_sociale` (
  `id_raison` int(11) NOT NULL,
  `raison` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `raison_sociale`
--

INSERT INTO `raison_sociale` (`id_raison`, `raison`) VALUES
(1, 'Bo Meuble'),
(2, 'Mobel'),
(3, 'Tout A la maison'),
(4, 'The World Compagny'),
(5, 'The Best Greatest Beautifulest Furniture');

-- --------------------------------------------------------

--
-- Structure de la table `site_de_production`
--

CREATE TABLE `site_de_production` (
  `id_site` int(11) NOT NULL,
  `nom` varchar(50) NOT NULL,
  `adresse_usine` varchar(70) NOT NULL,
  `id_ville` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `site_de_production`
--

INSERT INTO `site_de_production` (`id_site`, `nom`, `adresse_usine`, `id_ville`) VALUES
(1, 'Harald', 'Quai Pipervika', 1),
(2, 'Sverre', 'Rue Strangehagen', 2),
(3, 'Olaf', 'Place Nidaros', 3);

-- --------------------------------------------------------

--
-- Structure de la table `type`
--

CREATE TABLE `type` (
  `id_type` int(11) NOT NULL,
  `type` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `type`
--

INSERT INTO `type` (`id_type`, `type`) VALUES
(1, 'Magasin'),
(2, 'Centrale d\'achat');

-- --------------------------------------------------------

--
-- Structure de la table `ville`
--

CREATE TABLE `ville` (
  `id_ville` int(11) NOT NULL,
  `ville` varchar(30) NOT NULL,
  `pays` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `ville`
--

INSERT INTO `ville` (`id_ville`, `ville`, `pays`) VALUES
(1, 'Oslo', 'Norvège'),
(2, 'Bergen', 'Norvège'),
(3, 'Trondheim', 'Norvège'),
(4, 'Paris', 'France'),
(5, 'Berlin', 'Allemagne'),
(6, 'Brest', 'France'),
(7, 'Barcelone', 'Espagne'),
(8, 'Londres', 'Angleterre');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `clients`
--
ALTER TABLE `clients`
  ADD PRIMARY KEY (`id_client`),
  ADD KEY `raison_sociale_clients_fk` (`id_raison`),
  ADD KEY `type_clients_fk` (`id_type`),
  ADD KEY `ville_clients_fk` (`id_ville`);

--
-- Index pour la table `facture`
--
ALTER TABLE `facture`
  ADD PRIMARY KEY (`id_facture`),
  ADD KEY `id_client` (`id_client`);

--
-- Index pour la table `factures_produit`
--
ALTER TABLE `factures_produit`
  ADD PRIMARY KEY (`id_produit`,`id_facture`),
  ADD KEY `facture_factures_produit_fk` (`id_facture`);

--
-- Index pour la table `produits`
--
ALTER TABLE `produits`
  ADD PRIMARY KEY (`id_produit`);

--
-- Index pour la table `produit_site`
--
ALTER TABLE `produit_site`
  ADD KEY `produits_produit_site_fk` (`id_produit`),
  ADD KEY `site_de_production_produit_site_fk` (`id_site`);

--
-- Index pour la table `raison_sociale`
--
ALTER TABLE `raison_sociale`
  ADD PRIMARY KEY (`id_raison`);

--
-- Index pour la table `site_de_production`
--
ALTER TABLE `site_de_production`
  ADD PRIMARY KEY (`id_site`),
  ADD KEY `ville_site_de_production_fk` (`id_ville`);

--
-- Index pour la table `type`
--
ALTER TABLE `type`
  ADD PRIMARY KEY (`id_type`);

--
-- Index pour la table `ville`
--
ALTER TABLE `ville`
  ADD PRIMARY KEY (`id_ville`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `clients`
--
ALTER TABLE `clients`
  MODIFY `id_client` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT pour la table `facture`
--
ALTER TABLE `facture`
  MODIFY `id_facture` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT pour la table `produits`
--
ALTER TABLE `produits`
  MODIFY `id_produit` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT pour la table `raison_sociale`
--
ALTER TABLE `raison_sociale`
  MODIFY `id_raison` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT pour la table `site_de_production`
--
ALTER TABLE `site_de_production`
  MODIFY `id_site` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT pour la table `type`
--
ALTER TABLE `type`
  MODIFY `id_type` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT pour la table `ville`
--
ALTER TABLE `ville`
  MODIFY `id_ville` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `clients`
--
ALTER TABLE `clients`
  ADD CONSTRAINT `raison_sociale_clients_fk` FOREIGN KEY (`id_raison`) REFERENCES `raison_sociale` (`id_raison`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `type_clients_fk` FOREIGN KEY (`id_type`) REFERENCES `type` (`id_type`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `ville_clients_fk` FOREIGN KEY (`id_ville`) REFERENCES `ville` (`id_ville`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Contraintes pour la table `facture`
--
ALTER TABLE `facture`
  ADD CONSTRAINT `facture_ibfk_1` FOREIGN KEY (`id_client`) REFERENCES `clients` (`id_client`);

--
-- Contraintes pour la table `factures_produit`
--
ALTER TABLE `factures_produit`
  ADD CONSTRAINT `facture_factures_produit_fk` FOREIGN KEY (`id_facture`) REFERENCES `facture` (`id_facture`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `produits_factures_produit_fk` FOREIGN KEY (`id_produit`) REFERENCES `produits` (`id_produit`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Contraintes pour la table `produit_site`
--
ALTER TABLE `produit_site`
  ADD CONSTRAINT `produits_produit_site_fk` FOREIGN KEY (`id_produit`) REFERENCES `produits` (`id_produit`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `site_de_production_produit_site_fk` FOREIGN KEY (`id_site`) REFERENCES `site_de_production` (`id_site`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Contraintes pour la table `site_de_production`
--
ALTER TABLE `site_de_production`
  ADD CONSTRAINT `ville_site_de_production_fk` FOREIGN KEY (`id_ville`) REFERENCES `ville` (`id_ville`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
