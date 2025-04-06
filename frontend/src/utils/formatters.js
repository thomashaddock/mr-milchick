export const formatPrice = (price) => {
  if (!price) return "";
  return typeof price === "number" ? `$${price.toLocaleString()}` : price;
};

export const formatAddress = (address) => {
  if (!address) return "";
  return address.trim();
};
