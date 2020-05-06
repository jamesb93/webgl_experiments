echo "Yarning..."
yarn install
echo "Copying updated deps to dist..."
mkdir -p js/three
cp -r node_modules/three/ js/three/
