import React from "react";

const PropertyCard = ({ property }) => {
  return (
    <div className="property-card">
      <img
        src={property.imageUrl}
        alt={property.address}
        className="property-image"
      />
      <div className="property-details">
        <h4>{property.address}</h4>
        <p className="property-price">{property.price}</p>
        <p className="property-specs">
          {property.bedrooms} bed • {property.bathrooms} bath • {property.sqft}{" "}
          sq.ft
        </p>
        <button className="property-button">View Details</button>
      </div>
    </div>
  );
};

export default PropertyCard;
