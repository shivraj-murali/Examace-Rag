/** @type {import('next').NextConfig} */
const nextConfig = {
  images: {
    domains: [
      'm.media-amazon.com',
      'media.amazon.com',
      'images-na.ssl-images-amazon.com',
      'example.com'
    ],
    remotePatterns: [
      {
        protocol: 'https',
        hostname: '**.amazon.com',
        port: '',
        pathname: '/**',
      },
      {
        protocol: 'https',
        hostname: '**.media-amazon.com',
        port: '',
        pathname: '/**',
      },
    ],
  },
};

export default nextConfig;
