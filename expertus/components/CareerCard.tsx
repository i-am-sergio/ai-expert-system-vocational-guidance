import { FontAwesome } from '@expo/vector-icons';
import React from 'react';
import { Text, StyleSheet, TouchableOpacity, GestureResponderEvent, View } from 'react-native';

interface CareerCardProps {
  title: string;
  description: string;
}

const CareerCard: React.FC<CareerCardProps> = ({ title, description }) => {
  return (
    <TouchableOpacity style={styles.card}>
      <View style={styles.iconContainer}>
        <FontAwesome name="graduation-cap" size={24} color="#8948c7" />
      </View>
      <Text style={styles.cardTitle}>{title}</Text>
      <Text style={styles.cardDescription}>{description}</Text>
    </TouchableOpacity>
  );
};


const styles = StyleSheet.create({
  iconContainer: {
    marginBottom: 8,
  },
  card: {
    backgroundColor: '#fff',
    borderRadius: 8,
    padding: 16,
    margin: 8,
    shadowColor: '#000',
    shadowOpacity: 0.1,
    shadowRadius: 10,
    shadowOffset: { width: 0, height: 5 },
    elevation: 5,
    width: '45%',
  },
  cardTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    marginBottom: 8,
  },
  cardDescription: {
    fontSize: 14,
    color: '#666',
  },
});

export default CareerCard;