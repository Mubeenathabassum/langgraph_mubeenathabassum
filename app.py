Cloning from https://github.com/Mubeenathabassum/langgraph_mubeenathabassum

==> Checking out commit b691f481acaba6744fc1a7f5daec5fcd8517c492 in branch main

==> Using Python version 3.14.3 (default)

==> Docs on specifying a Python version: https://render.com/docs/python-version

==> Installing Python version 3.14.3...

==> Using Poetry version 2.1.3 (default)

==> Docs on specifying a Poetry version: https://render.com/docs/poetry-version

==> Running build command 'pip install -r requirements.txt'...

Collecting fastapi (from -r requirements.txt (line 1))

Downloading fastapi-0.141.1-py3-none-any.whl.metadata (27 kB)

Collecting uvicorn (from -r requirements.txt (line 2))

Downloading uvicorn-0.53.0-py3-none-any.whl.metadata (6.6 kB)

Collecting langchain (from -r requirements.txt (line 3))

Downloading langchain-1.4.2-py3-none-any.whl.metadata (6.2 kB)

Collecting langgraph (from -r requirements.txt (line 4))

Downloading langgraph-1.2.12-py3-none-any.whl.metadata (4.9 kB)

Collecting langchain-google-genai (from -r requirements.txt (line 5))

Downloading langchain_google_genai-4.4.0-py3-none-any.whl.metadata (2.7 kB)

Collecting google-generativeai (from -r requirements.txt (line 6))

Downloading google_generativeai-0.8.6-py3-none-any.whl.metadata (3.9 kB)

Collecting pydantic (from -r requirements.txt (line 7))

Downloading pydantic-2.13.5-py3-none-any.whl.metadata (110 kB)

Collecting starlette>=0.46.0 (from fastapi->-r requirements.txt (line 1))

Downloading starlette-1.7.0-py3-none-any.whl.metadata (6.6 kB)

Collecting typing-extensions>=4.8.0 (from fastapi->-r requirements.txt (line 1))

Downloading typing_extensions-4.16.0-py3-none-any.whl.metadata (3.3 kB)

Collecting typing-inspection>=0.4.2 (from fastapi->-r requirements.txt (line 1))

Downloading typing_inspection-0.4.4-py3-none-any.whl.metadata (2.6 kB)

Collecting annotated-doc>=0.0.2 (from fastapi->-r requirements.txt (line 1))

Downloading annotated_doc-0.0.5-py3-none-any.whl.metadata (6.5 kB)

Collecting click>=7.0 (from uvicorn->-r requirements.txt (line 2))

Downloading click-8.5.0-py3-none-any.whl.metadata (2.6 kB)

Collecting h11>=0.8 (from uvicorn->-r requirements.txt (line 2))

Downloading h11-0.16.0-py3-none-any.whl.metadata (8.3 kB)

Collecting langchain-core<2.0.0,>=1.6.3 (from langchain->-r requirements.txt (line 3))

Downloading langchain_core-1.6.5-py3-none-any.whl.metadata (4.8 kB)

Collecting langgraph-checkpoint<5.0.0,>=4.1.0 (from langgraph->-r requirements.txt (line 4))

Downloading langgraph_checkpoint-4.2.0-py3-none-any.whl.metadata (6.7 kB)

Collecting langgraph-prebuilt<1.2.0,>=1.1.0 (from langgraph->-r requirements.txt (line 4))

Downloading langgraph_prebuilt-1.1.0-py3-none-any.whl.metadata (5.2 kB)

Collecting langgraph-sdk<0.5.0,>=0.4.2 (from langgraph->-r requirements.txt (line 4))

Downloading langgraph_sdk-0.4.5-py3-none-any.whl.metadata (5.1 kB)

Collecting xxhash>=3.5.0 (from langgraph->-r requirements.txt (line 4))

Downloading xxhash-4.0.1-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (17 kB)

Collecting annotated-types>=0.6.0 (from pydantic->-r requirements.txt (line 7))

Downloading annotated_types-0.8.0-py3-none-any.whl.metadata (15 kB)

Collecting pydantic-core==2.46.5 (from pydantic->-r requirements.txt (line 7))

Downloading pydantic_core-2.46.5-cp314-cp314-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (6.6 kB)

Collecting httpx<1.0.0,>=0.23.0 (from langchain-core<2.0.0,>=1.6.3->langchain->-r requirements.txt (line 3))

Downloading httpx-0.28.1-py3-none-any.whl.metadata (7.1 kB)

Collecting jsonpatch<2.0.0,>=1.33.0 (from langchain-core<2.0.0,>=1.6.3->langchain->-r requirements.txt (line 3))

Downloading jsonpatch-1.33-py2.py3-none-any.whl.metadata (3.0 kB)

Collecting langchain-protocol>=0.0.17 (from langchain-core<2.0.0,>=1.6.3->langchain->-r requirements.txt (line 3))

Downloading langchain_protocol-0.0.19-py3-none-any.whl.metadata (2.4 kB)

Collecting langsmith<1.0.0,>=0.3.45 (from langchain-core<2.0.0,>=1.6.3->langchain->-r requirements.txt (line 3))

Downloading langsmith-0.14.0-py3-none-any.whl.metadata (22 kB)

Collecting packaging>=23.2.0 (from langchain-core<2.0.0,>=1.6.3->langchain->-r requirements.txt (line 3))

Downloading packaging-26.3-py3-none-any.whl.metadata (3.5 kB)

Collecting pyyaml<7.0.0,>=5.3.0 (from langchain-core<2.0.0,>=1.6.3->langchain->-r requirements.txt (line 3))

Downloading pyyaml-6.0.3-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (2.4 kB)

Collecting tenacity!=8.4.0,<10.0.0,>=8.1.0 (from langchain-core<2.0.0,>=1.6.3->langchain->-r requirements.txt (line 3))

Downloading tenacity-9.1.4-py3-none-any.whl.metadata (1.2 kB)

Collecting uuid-utils<1.0,>=0.12.0 (from langchain-core<2.0.0,>=1.6.3->langchain->-r requirements.txt (line 3))

Downloading uuid_utils-0.17.1-cp314-cp314-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (6.4 kB)

Collecting anyio (from httpx<1.0.0,>=0.23.0->langchain-core<2.0.0,>=1.6.3->langchain->-r requirements.txt (line 3))

Downloading anyio-4.15.1-py3-none-any.whl.metadata (4.7 kB)

Collecting certifi (from httpx<1.0.0,>=0.23.0->langchain-core<2.0.0,>=1.6.3->langchain->-r requirements.txt (line 3))

Downloading certifi-2026.7.22-py3-none-any.whl.metadata (2.5 kB)

Collecting httpcore==1.* (from httpx<1.0.0,>=0.23.0->langchain-core<2.0.0,>=1.6.3->langchain->-r requirements.txt (line 3))

Downloading httpcore-1.0.9-py3-none-any.whl.metadata (21 kB)

Collecting idna (from httpx<1.0.0,>=0.23.0->langchain-core<2.0.0,>=1.6.3->langchain->-r requirements.txt (line 3))

Downloading idna-3.20-py3-none-any.whl.metadata (7.2 kB)

Collecting jsonpointer>=1.9 (from jsonpatch<2.0.0,>=1.33.0->langchain-core<2.0.0,>=1.6.3->langchain->-r requirements.txt (line 3))

Downloading jsonpointer-3.1.1-py3-none-any.whl.metadata (2.4 kB)

Collecting ormsgpack>=1.12.0 (from langgraph-checkpoint<5.0.0,>=4.1.0->langgraph->-r requirements.txt (line 4))

Downloading ormsgpack-1.12.2-cp314-cp314-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (3.2 kB)

Collecting orjson>=3.11.5 (from langgraph-sdk<0.5.0,>=0.4.2->langgraph->-r requirements.txt (line 4))

Downloading orjson-3.12.0-cp314-cp314-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (41 kB)

Collecting websockets<17,>=14 (from langgraph-sdk<0.5.0,>=0.4.2->langgraph->-r requirements.txt (line 4))

Downloading websockets-16.1.1-cp314-cp314-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl.metadata (6.8 kB)

Collecting distro>=1.7.0 (from langsmith<1.0.0,>=0.3.45->langchain-core<2.0.0,>=1.6.3->langchain->-r requirements.txt (line 3))

Downloading distro-1.9.0-py3-none-any.whl.metadata (6.8 kB)

Collecting httpx2<3,>=2 (from langsmith<1.0.0,>=0.3.45->langchain-core<2.0.0,>=1.6.3->langchain->-r requirements.txt (line 3))

Downloading httpx2-2.13.1-py3-none-any.whl.metadata (9.8 kB)

Collecting requests-toolbelt>=1.0.0 (from langsmith<1.0.0,>=0.3.45->langchain-core<2.0.0,>=1.6.3->langchain->-r requirements.txt (line 3))

Downloading requests_toolbelt-1.0.0-py2.py3-none-any.whl.metadata (14 kB)

Collecting requests>=2.0.0 (from langsmith<1.0.0,>=0.3.45->langchain-core<2.0.0,>=1.6.3->langchain->-r requirements.txt (line 3))

Downloading requests-2.34.2-py3-none-any.whl.metadata (4.8 kB)

Collecting sniffio>=1.1 (from langsmith<1.0.0,>=0.3.45->langchain-core<2.0.0,>=1.6.3->langchain->-r requirements.txt (line 3))

Downloading sniffio-1.3.1-py3-none-any.whl.metadata (3.9 kB)

Collecting zstandard>=0.23.0 (from langsmith<1.0.0,>=0.3.45->langchain-core<2.0.0,>=1.6.3->langchain->-r requirements.txt (line 3))

Downloading zstandard-0.25.0-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (3.3 kB)

Collecting httpcore2==2.13.1 (from httpx2<3,>=2->langsmith<1.0.0,>=0.3.45->langchain-core<2.0.0,>=1.6.3->langchain->-r requirements.txt (line 3))

Downloading httpcore2-2.13.1-py3-none-any.whl.metadata (26 kB)

Collecting truststore>=0.10 (from httpx2<3,>=2->langsmith<1.0.0,>=0.3.45->langchain-core<2.0.0,>=1.6.3->langchain->-r requirements.txt (line 3))

Downloading truststore-0.10.4-py3-none-any.whl.metadata (4.4 kB)

Collecting filetype<2.0.0,>=1.2.0 (from langchain-google-genai->-r requirements.txt (line 5))

Downloading filetype-1.2.0-py2.py3-none-any.whl.metadata (6.5 kB)

Collecting google-genai<3.0.0,>=2.20.0 (from langchain-google-genai->-r requirements.txt (line 5))

Downloading google_genai-2.25.0-py3-none-any.whl.metadata (56 kB)

Collecting google-auth<3.0.0,>=2.56.0 (from google-auth[requests]<3.0.0,>=2.56.0->google-genai<3.0.0,>=2.20.0->langchain-google-genai->-r requirements.txt (line 5))

Downloading google_auth-2.58.1-py3-none-any.whl.metadata (6.0 kB)

Collecting pyasn1-modules>=0.2.1 (from google-auth<3.0.0,>=2.56.0->google-auth[requests]<3.0.0,>=2.56.0->google-genai<3.0.0,>=2.20.0->langchain-google-genai->-r requirements.txt (line 5))

Downloading pyasn1_modules-0.4.2-py3-none-any.whl.metadata (3.5 kB)

Collecting cryptography>=41.0.5 (from google-auth<3.0.0,>=2.56.0->google-auth[requests]<3.0.0,>=2.56.0->google-genai<3.0.0,>=2.20.0->langchain-google-genai->-r requirements.txt (line 5))

Downloading cryptography-50.0.1-cp311-abi3-manylinux_2_34_x86_64.whl.metadata (4.3 kB)

Collecting charset_normalizer<4,>=2 (from requests>=2.0.0->langsmith<1.0.0,>=0.3.45->langchain-core<2.0.0,>=1.6.3->langchain->-r requirements.txt (line 3))

Downloading charset_normalizer-3.5.1-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (45 kB)

Collecting urllib3<3,>=1.26 (from requests>=2.0.0->langsmith<1.0.0,>=0.3.45->langchain-core<2.0.0,>=1.6.3->langchain->-r requirements.txt (line 3))

Downloading urllib3-2.8.0-py3-none-any.whl.metadata (7.4 kB)

Collecting google-ai-generativelanguage==0.6.15 (from google-generativeai->-r requirements.txt (line 6))

Downloading google_ai_generativelanguage-0.6.15-py3-none-any.whl.metadata (5.7 kB)

Collecting google-api-core (from google-generativeai->-r requirements.txt (line 6))

Downloading google_api_core-2.39.0-py3-none-any.whl.metadata (3.2 kB)

Collecting google-api-python-client (from google-generativeai->-r requirements.txt (line 6))

Downloading google_api_python_client-2.200.0-py3-none-any.whl.metadata (6.8 kB)

Collecting protobuf (from google-generativeai->-r requirements.txt (line 6))

Downloading protobuf-7.36.2-cp310-abi3-manylinux2014_x86_64.whl.metadata (595 bytes)

Collecting tqdm (from google-generativeai->-r requirements.txt (line 6))

Downloading tqdm-4.70.1-py3-none-any.whl.metadata (57 kB)

Collecting proto-plus<2.0.0dev,>=1.22.3 (from google-ai-generativelanguage==0.6.15->google-generativeai->-r requirements.txt (line 6))

Downloading proto_plus-1.28.4-py3-none-any.whl.metadata (2.2 kB)

Collecting protobuf (from google-generativeai->-r requirements.txt (line 6))

Downloading protobuf-5.29.6-cp38-abi3-manylinux2014_x86_64.whl.metadata (592 bytes)

Collecting googleapis-common-protos<2.0.0,>=1.69.2 (from google-api-core->google-generativeai->-r requirements.txt (line 6))

Downloading googleapis_common_protos-1.75.4-py3-none-any.whl.metadata (8.5 kB)

INFO: pip is looking at multiple versions of google-api-core to determine which version is compatible with other requirements. This could take a while.

Collecting google-api-core (from google-generativeai->-r requirements.txt (line 6))

Downloading google_api_core-2.38.0-py3-none-any.whl.metadata (3.2 kB)

Downloading google_api_core-2.37.0-py3-none-any.whl.metadata (3.2 kB)

Downloading google_api_core-2.36.0-py3-none-any.whl.metadata (3.2 kB)

Downloading google_api_core-2.34.0-py3-none-any.whl.metadata (2.9 kB)

Downloading google_api_core-2.33.0-py3-none-any.whl.metadata (3.2 kB)

INFO: pip is looking at multiple versions of google-api-core[grpc] to determine which version is compatible with other requirements. This could take a while.

Collecting grpcio<2.0.0,>=1.41.0 (from google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.10.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,!=2.8.*,!=2.9.*,<3.0.0dev,>=1.34.1->google-ai-generativelanguage==0.6.15->google-generativeai->-r requirements.txt (line 6))

Downloading grpcio-1.84.0-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (3.8 kB)

Collecting grpcio-status<2.0.0,>=1.41.0 (from google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.10.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,!=2.8.*,!=2.9.*,<3.0.0dev,>=1.34.1->google-ai-generativelanguage==0.6.15->google-generativeai->-r requirements.txt (line 6))

Downloading grpcio_status-1.84.0-py3-none-any.whl.metadata (1.3 kB)

INFO: pip is looking at multiple versions of googleapis-common-protos to determine which version is compatible with other requirements. This could take a while.

Collecting googleapis-common-protos<2.0.0,>=1.63.2 (from google-api-core->google-generativeai->-r requirements.txt (line 6))

Downloading googleapis_common_protos-1.75.3-py3-none-any.whl.metadata (8.5 kB)

Downloading googleapis_common_protos-1.75.2-py3-none-any.whl.metadata (8.5 kB)

Downloading googleapis_common_protos-1.75.1-py3-none-any.whl.metadata (8.5 kB)

Downloading googleapis_common_protos-1.75.0-py3-none-any.whl.metadata (8.6 kB)

INFO: pip is looking at multiple versions of grpcio-status to determine which version is compatible with other requirements. This could take a while.

Collecting grpcio-status<2.0.0,>=1.41.0 (from google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.10.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,!=2.8.*,!=2.9.*,<3.0.0dev,>=1.34.1->google-ai-generativelanguage==0.6.15->google-generativeai->-r requirements.txt (line 6))

Downloading grpcio_status-1.83.1-py3-none-any.whl.metadata (1.2 kB)

Downloading grpcio_status-1.83.0-py3-none-any.whl.metadata (1.2 kB)

Downloading grpcio_status-1.82.2-py3-none-any.whl.metadata (1.2 kB)

Downloading grpcio_status-1.82.1-py3-none-any.whl.metadata (1.2 kB)

Downloading grpcio_status-1.81.1-py3-none-any.whl.metadata (1.2 kB)

Downloading grpcio_status-1.81.0-py3-none-any.whl.metadata (1.2 kB)

Downloading grpcio_status-1.80.0-py3-none-any.whl.metadata (1.3 kB)

INFO: pip is still looking at multiple versions of grpcio-status to determine which version is compatible with other requirements. This could take a while.

Downloading grpcio_status-1.78.0-py3-none-any.whl.metadata (1.3 kB)

Downloading grpcio_status-1.76.0-py3-none-any.whl.metadata (1.1 kB)

Downloading grpcio_status-1.75.1-py3-none-any.whl.metadata (1.1 kB)

INFO: pip is still looking at multiple versions of googleapis-common-protos to determine which version is compatible with other requirements. This could take a while.

Collecting googleapis-common-protos<2.0.0,>=1.63.2 (from google-api-core->google-generativeai->-r requirements.txt (line 6))

Downloading googleapis_common_protos-1.74.0-py3-none-any.whl.metadata (9.2 kB)

INFO: This is taking longer than usual. You might need to provide the dependency resolver with stricter constraints to reduce runtime. See https://pip.pypa.io/warnings/backtracking for guidance. If you want to abort this run, press Ctrl + C.

Downloading googleapis_common_protos-1.73.1-py3-none-any.whl.metadata (9.2 kB)

INFO: This is taking longer than usual. You might need to provide the dependency resolver with stricter constraints to reduce runtime. See https://pip.pypa.io/warnings/backtracking for guidance. If you want to abort this run, press Ctrl + C.

Downloading googleapis_common_protos-1.73.0-py3-none-any.whl.metadata (9.4 kB)

Downloading googleapis_common_protos-1.72.0-py3-none-any.whl.metadata (9.4 kB)

Downloading googleapis_common_protos-1.71.0-py3-none-any.whl.metadata (9.4 kB)

Downloading googleapis_common_protos-1.70.0-py3-none-any.whl.metadata (9.3 kB)

Downloading googleapis_common_protos-1.69.2-py3-none-any.whl.metadata (9.3 kB)

Downloading googleapis_common_protos-1.69.1-py2.py3-none-any.whl.metadata (9.3 kB)

Downloading googleapis_common_protos-1.69.0-py2.py3-none-any.whl.metadata (5.1 kB)

Downloading googleapis_common_protos-1.68.0-py2.py3-none-any.whl.metadata (5.1 kB)

Downloading googleapis_common_protos-1.67.0-py2.py3-none-any.whl.metadata (5.1 kB)

Downloading googleapis_common_protos-1.66.0-py2.py3-none-any.whl.metadata (1.5 kB)

Downloading googleapis_common_protos-1.65.0-py2.py3-none-any.whl.metadata (1.5 kB)

Downloading googleapis_common_protos-1.64.0-py2.py3-none-any.whl.metadata (1.5 kB)

Downloading googleapis_common_protos-1.63.2-py2.py3-none-any.whl.metadata (1.5 kB)

INFO: pip is still looking at multiple versions of google-api-core[grpc] to determine which version is compatible with other requirements. This could take a while.

Collecting google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.10.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,!=2.8.*,!=2.9.*,<3.0.0dev,>=1.34.1 (from google-ai-generativelanguage==0.6.15->google-generativeai->-r requirements.txt (line 6))

Downloading google_api_core-2.32.0-py3-none-any.whl.metadata (3.2 kB)

INFO: This is taking longer than usual. You might need to provide the dependency resolver with stricter constraints to reduce runtime. See https://pip.pypa.io/warnings/backtracking for guidance. If you want to abort this run, press Ctrl + C.

Downloading google_api_core-2.31.0-py3-none-any.whl.metadata (3.2 kB)

Downloading google_api_core-2.30.3-py3-none-any.whl.metadata (3.1 kB)

Downloading google_api_core-2.30.2-py3-none-any.whl.metadata (3.1 kB)

Downloading google_api_core-2.30.1-py3-none-any.whl.metadata (3.1 kB)

Downloading google_api_core-2.30.0-py3-none-any.whl.metadata (3.1 kB)

Collecting googleapis-common-protos<2.0.0,>=1.56.3 (from google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.10.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,!=2.8.*,!=2.9.*,<3.0.0dev,>=1.34.1->google-ai-generativelanguage==0.6.15->google-generativeai->-r requirements.txt (line 6))

Downloading googleapis_common_protos-1.63.1-py2.py3-none-any.whl.metadata (1.5 kB)

Downloading googleapis_common_protos-1.63.0-py2.py3-none-any.whl.metadata (1.5 kB)

Collecting protobuf (from google-generativeai->-r requirements.txt (line 6))

Downloading protobuf-4.25.9-cp37-abi3-manylinux2014_x86_64.whl.metadata (541 bytes)

Collecting googleapis-common-protos<2.0.0,>=1.56.3 (from google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.10.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,!=2.8.*,!=2.9.*,<3.0.0dev,>=1.34.1->google-ai-generativelanguage==0.6.15->google-generativeai->-r requirements.txt (line 6))

Downloading googleapis_common_protos-1.62.0-py2.py3-none-any.whl.metadata (1.5 kB)

Downloading googleapis_common_protos-1.61.0-py2.py3-none-any.whl.metadata (1.5 kB)

Downloading googleapis_common_protos-1.60.0-py2.py3-none-any.whl.metadata (1.5 kB)

Downloading googleapis_common_protos-1.59.1-py2.py3-none-any.whl.metadata (1.5 kB)

Downloading googleapis_common_protos-1.59.0-py2.py3-none-any.whl.metadata (1.5 kB)

Downloading googleapis_common_protos-1.58.0-py2.py3-none-any.whl.metadata (1.5 kB)

Downloading googleapis_common_protos-1.57.1-py2.py3-none-any.whl.metadata (1.5 kB)

Downloading googleapis_common_protos-1.57.0-py2.py3-none-any.whl.metadata (1.5 kB)

Downloading googleapis_common_protos-1.56.4-py2.py3-none-any.whl.metadata (1.3 kB)

Downloading googleapis_common_protos-1.56.3-py2.py3-none-any.whl.metadata (1.3 kB)

Collecting google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.10.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,!=2.8.*,!=2.9.*,<3.0.0dev,>=1.34.1 (from google-ai-generativelanguage==0.6.15->google-generativeai->-r requirements.txt (line 6))

Downloading google_api_core-2.29.0-py3-none-any.whl.metadata (3.3 kB)

Collecting googleapis-common-protos<2.0.0,>=1.56.2 (from google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.10.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,!=2.8.*,!=2.9.*,<3.0.0dev,>=1.34.1->google-ai-generativelanguage==0.6.15->google-generativeai->-r requirements.txt (line 6))

Downloading googleapis_common_protos-1.56.2-py2.py3-none-any.whl.metadata (1.3 kB)

Collecting protobuf (from google-generativeai->-r requirements.txt (line 6))

Downloading protobuf-3.20.3-py2.py3-none-any.whl.metadata (720 bytes)

Collecting google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.10.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,!=2.8.*,!=2.9.*,<3.0.0dev,>=1.34.1 (from google-ai-generativelanguage==0.6.15->google-generativeai->-r requirements.txt (line 6))

Downloading google_api_core-2.28.1-py3-none-any.whl.metadata (3.3 kB)

Downloading google_api_core-2.28.0-py3-none-any.whl.metadata (3.2 kB)

Downloading google_api_core-2.27.0-py3-none-any.whl.metadata (3.2 kB)

Downloading google_api_core-2.26.0-py3-none-any.whl.metadata (3.2 kB)

Downloading google_api_core-2.25.2-py3-none-any.whl.metadata (3.0 kB)

Collecting grpcio-status<2.0.0,>=1.33.2 (from google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.10.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,!=2.8.*,!=2.9.*,<3.0.0dev,>=1.34.1->google-ai-generativelanguage==0.6.15->google-generativeai->-r requirements.txt (line 6))

Downloading grpcio_status-1.75.0-py3-none-any.whl.metadata (1.1 kB)

Downloading grpcio_status-1.74.0-py3-none-any.whl.metadata (1.1 kB)

Downloading grpcio_status-1.73.1-py3-none-any.whl.metadata (1.1 kB)

Downloading grpcio_status-1.73.0-py3-none-any.whl.metadata (1.1 kB)

Downloading grpcio_status-1.72.2-py3-none-any.whl.metadata (1.1 kB)

Downloading grpcio_status-1.72.1-py3-none-any.whl.metadata (1.1 kB)

Downloading grpcio_status-1.71.2-py3-none-any.whl.metadata (1.1 kB)

INFO: pip is looking at multiple versions of proto-plus to determine which version is compatible with other requirements. This could take a while.

Collecting proto-plus<2.0.0dev,>=1.22.3 (from google-ai-generativelanguage==0.6.15->google-generativeai->-r requirements.txt (line 6))

Downloading proto_plus-1.28.3-py3-none-any.whl.metadata (2.2 kB)

Downloading proto_plus-1.28.2-py3-none-any.whl.metadata (2.2 kB)

Collecting cffi>=2.0.0 (from cryptography>=41.0.5->google-auth<3.0.0,>=2.56.0->google-auth[requests]<3.0.0,>=2.56.0->google-genai<3.0.0,>=2.20.0->langchain-google-genai->-r requirements.txt (line 5))

Downloading cffi-2.1.1-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (2.5 kB)

Collecting pycparser (from cffi>=2.0.0->cryptography>=41.0.5->google-auth<3.0.0,>=2.56.0->google-auth[requests]<3.0.0,>=2.56.0->google-genai<3.0.0,>=2.20.0->langchain-google-genai->-r requirements.txt (line 5))

Downloading pycparser-3.0-py3-none-any.whl.metadata (8.2 kB)

Collecting pyasn1<0.7.0,>=0.6.1 (from pyasn1-modules>=0.2.1->google-auth<3.0.0,>=2.56.0->google-auth[requests]<3.0.0,>=2.56.0->google-genai<3.0.0,>=2.20.0->langchain-google-genai->-r requirements.txt (line 5))

Downloading pyasn1-0.6.4-py3-none-any.whl.metadata (8.4 kB)

Collecting httplib2<1.0.0,>=0.19.0 (from google-api-python-client->google-generativeai->-r requirements.txt (line 6))

Downloading httplib2-0.32.0-py3-none-any.whl.metadata (2.2 kB)

Collecting google-auth-httplib2<1.0.0,>=0.2.0 (from google-api-python-client->google-generativeai->-r requirements.txt (line 6))

Downloading google_auth_httplib2-0.4.2-py3-none-any.whl.metadata (3.0 kB)

Collecting uritemplate<5,>=3.0.1 (from google-api-python-client->google-generativeai->-r requirements.txt (line 6))

Downloading uritemplate-4.2.0-py3-none-any.whl.metadata (2.6 kB)

Collecting pyparsing<4,>=3.1 (from httplib2<1.0.0,>=0.19.0->google-api-python-client->google-generativeai->-r requirements.txt (line 6))

Downloading pyparsing-3.3.3-py3-none-any.whl.metadata (5.9 kB)

Downloading fastapi-0.141.1-py3-none-any.whl (131 kB)

Downloading uvicorn-0.53.0-py3-none-any.whl (87 kB)

Downloading langchain-1.4.2-py3-none-any.whl (163 kB)

Downloading langgraph-1.2.12-py3-none-any.whl (250 kB)

Downloading pydantic-2.13.5-py3-none-any.whl (472 kB)

Downloading pydantic_core-2.46.5-cp314-cp314-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.1 MB)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.1/2.1 MB 16.2 MB/s  0:00:00

Downloading langchain_core-1.6.5-py3-none-any.whl (572 kB)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 572.1/572.1 kB 21.8 MB/s  0:00:00

Downloading httpx-0.28.1-py3-none-any.whl (73 kB)

Downloading httpcore-1.0.9-py3-none-any.whl (78 kB)

Downloading jsonpatch-1.33-py2.py3-none-any.whl (12 kB)

Downloading langgraph_checkpoint-4.2.0-py3-none-any.whl (56 kB)

Downloading langgraph_prebuilt-1.1.0-py3-none-any.whl (41 kB)

Downloading langgraph_sdk-0.4.5-py3-none-any.whl (162 kB)

Downloading langsmith-0.14.0-py3-none-any.whl (805 kB)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 805.0/805.0 kB 25.0 MB/s  0:00:00

Downloading httpx2-2.13.1-py3-none-any.whl (95 kB)

Downloading httpcore2-2.13.1-py3-none-any.whl (83 kB)

Downloading pyyaml-6.0.3-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (794 kB)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 794.2/794.2 kB 26.0 MB/s  0:00:00

Downloading tenacity-9.1.4-py3-none-any.whl (28 kB)

Downloading typing_extensions-4.16.0-py3-none-any.whl (45 kB)

Downloading uuid_utils-0.17.1-cp314-cp314-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (325 kB)

Downloading websockets-16.1.1-cp314-cp314-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl (187 kB)

Downloading langchain_google_genai-4.4.0-py3-none-any.whl (81 kB)

Downloading filetype-1.2.0-py2.py3-none-any.whl (19 kB)

Downloading google_genai-2.25.0-py3-none-any.whl (1.2 MB)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 31.5 MB/s  0:00:00

Downloading anyio-4.15.1-py3-none-any.whl (132 kB)

Downloading distro-1.9.0-py3-none-any.whl (20 kB)

Downloading google_auth-2.58.1-py3-none-any.whl (262 kB)

Downloading requests-2.34.2-py3-none-any.whl (73 kB)

Downloading charset_normalizer-3.5.1-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (251 kB)

Downloading idna-3.20-py3-none-any.whl (69 kB)

Downloading urllib3-2.8.0-py3-none-any.whl (135 kB)

Downloading google_generativeai-0.8.6-py3-none-any.whl (155 kB)

Downloading google_ai_generativelanguage-0.6.15-py3-none-any.whl (1.3 MB)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.3/1.3 MB 36.1 MB/s  0:00:00

Downloading google_api_core-2.25.2-py3-none-any.whl (162 kB)

Downloading googleapis_common_protos-1.75.0-py3-none-any.whl (300 kB)

Downloading protobuf-5.29.6-cp38-abi3-manylinux2014_x86_64.whl (320 kB)

Downloading grpcio-1.84.0-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (7.2 MB)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.2/7.2 MB 55.3 MB/s  0:00:00

Downloading grpcio_status-1.71.2-py3-none-any.whl (14 kB)

Downloading proto_plus-1.28.2-py3-none-any.whl (50 kB)

Downloading annotated_doc-0.0.5-py3-none-any.whl (5.3 kB)

Downloading annotated_types-0.8.0-py3-none-any.whl (13 kB)

Downloading certifi-2026.7.22-py3-none-any.whl (136 kB)

Downloading click-8.5.0-py3-none-any.whl (125 kB)

Downloading cryptography-50.0.1-cp311-abi3-manylinux_2_34_x86_64.whl (4.7 MB)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.7/4.7 MB 80.1 MB/s  0:00:00

Downloading cffi-2.1.1-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (221 kB)

Downloading h11-0.16.0-py3-none-any.whl (37 kB)

Downloading jsonpointer-3.1.1-py3-none-any.whl (7.7 kB)

Downloading langchain_protocol-0.0.19-py3-none-any.whl (7.3 kB)

Downloading orjson-3.12.0-cp314-cp314-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (131 kB)

Downloading ormsgpack-1.12.2-cp314-cp314-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (212 kB)

Downloading packaging-26.3-py3-none-any.whl (129 kB)

Downloading pyasn1_modules-0.4.2-py3-none-any.whl (181 kB)

Downloading pyasn1-0.6.4-py3-none-any.whl (84 kB)

Downloading requests_toolbelt-1.0.0-py2.py3-none-any.whl (54 kB)

Downloading sniffio-1.3.1-py3-none-any.whl (10 kB)

Downloading starlette-1.7.0-py3-none-any.whl (78 kB)

Downloading truststore-0.10.4-py3-none-any.whl (18 kB)

Downloading typing_inspection-0.4.4-py3-none-any.whl (14 kB)

Downloading xxhash-4.0.1-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (268 kB)

Downloading zstandard-0.25.0-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (5.6 MB)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.6/5.6 MB 102.0 MB/s  0:00:00

Downloading google_api_python_client-2.200.0-py3-none-any.whl (16.1 MB)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 16.1/16.1 MB 146.3 MB/s  0:00:00

Downloading google_auth_httplib2-0.4.2-py3-none-any.whl (9.5 kB)

Downloading httplib2-0.32.0-py3-none-any.whl (93 kB)

Downloading pyparsing-3.3.3-py3-none-any.whl (126 kB)

Downloading uritemplate-4.2.0-py3-none-any.whl (11 kB)

Downloading pycparser-3.0-py3-none-any.whl (48 kB)

Downloading tqdm-4.70.1-py3-none-any.whl (80 kB)

Installing collected packages: filetype, zstandard, xxhash, websockets, uuid-utils, urllib3, uritemplate, typing-extensions, truststore, tqdm, tenacity, sniffio, pyyaml, pyparsing, pycparser, pyasn1, protobuf, packaging, ormsgpack, orjson, jsonpointer, idna, h11, distro, click, charset_normalizer, certifi, annotated-types, annotated-doc, uvicorn, typing-inspection, requests, pydantic-core, pyasn1-modules, proto-plus, langchain-protocol, jsonpatch, httplib2, httpcore2, httpcore, grpcio, googleapis-common-protos, cffi, anyio, starlette, requests-toolbelt, pydantic, httpx2, httpx, grpcio-status, cryptography, langsmith, google-auth, fastapi, langchain-core, google-auth-httplib2, google-api-core, langgraph-sdk, langgraph-checkpoint, google-genai, google-api-python-client, langgraph-prebuilt, langchain-google-genai, google-ai-generativelanguage, langgraph, google-generativeai, langchain

Successfully installed annotated-doc-0.0.5 annotated-types-0.8.0 anyio-4.15.1 certifi-2026.7.22 cffi-2.1.1 charset_normalizer-3.5.1 click-8.5.0 cryptography-50.0.1 distro-1.9.0 fastapi-0.141.1 filetype-1.2.0 google-ai-generativelanguage-0.6.15 google-api-core-2.25.2 google-api-python-client-2.200.0 google-auth-2.58.1 google-auth-httplib2-0.4.2 google-genai-2.25.0 google-generativeai-0.8.6 googleapis-common-protos-1.75.0 grpcio-1.84.0 grpcio-status-1.71.2 h11-0.16.0 httpcore-1.0.9 httpcore2-2.13.1 httplib2-0.32.0 httpx-0.28.1 httpx2-2.13.1 idna-3.20 jsonpatch-1.33 jsonpointer-3.1.1 langchain-1.4.2 langchain-core-1.6.5 langchain-google-genai-4.4.0 langchain-protocol-0.0.19 langgraph-1.2.12 langgraph-checkpoint-4.2.0 langgraph-prebuilt-1.1.0 langgraph-sdk-0.4.5 langsmith-0.14.0 orjson-3.12.0 ormsgpack-1.12.2 packaging-26.3 proto-plus-1.28.2 protobuf-5.29.6 pyasn1-0.6.4 pyasn1-modules-0.4.2 pycparser-3.0 pydantic-2.13.5 pydantic-core-2.46.5 pyparsing-3.3.3 pyyaml-6.0.3 requests-2.34.2 requests-toolbelt-1.0.0 sniffio-1.3.1 starlette-1.7.0 tenacity-9.1.4 tqdm-4.70.1 truststore-0.10.4 typing-extensions-4.16.0 typing-inspection-0.4.4 uritemplate-4.2.0 urllib3-2.8.0 uuid-utils-0.17.1 uvicorn-0.53.0 websockets-16.1.1 xxhash-4.0.1 zstandard-0.25.0

[notice] A new release of pip is available: 25.3 -> 26.2.1

[notice] To update, run: pip install --upgrade pip

==> Uploading build...

==> Uploaded in 5.2s. Compression took 1.7s

==> Build successful 🎉

==> Deploying...

==> Setting WEB_CONCURRENCY=1 by default, based on available CPUs in the instance

==> Running 'uvicorn app:app --host 0.0.0.0 --port $PORT'

Traceback (most recent call last):

File "/opt/render/project/src/.venv/bin/uvicorn", line 7, in <module>

sys.exit(main())

         \~\~\~\~^^

File "/opt/render/project/src/.venv/lib/python3.14/site-packages/click/core.py", line 1631, in __call__

return self.main(\*args, \*\*kwargs)

       \~\~\~\~\~\~\~\~\~^^^^^^^^^^^^^^^^^

File "/opt/render/project/src/.venv/lib/python3.14/site-packages/click/core.py", line 1552, in main

rv = self.invoke(ctx)

File "/opt/render/project/src/.venv/lib/python3.14/site-packages/click/core.py", line 1415, in invoke

return ctx.invoke(self.callback, \*\*ctx.params)

       \~\~\~\~\~\~\~\~\~\~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

File "/opt/render/project/src/.venv/lib/python3.14/site-packages/click/core.py", line 910, in invoke

return callback(\*args, \*\*kwargs)

File "/opt/render/project/src/.venv/lib/python3.14/site-packages/uvicorn/main.py", line 448, in main

run(

\~\~\~^

    app,

    ^^^^

...<49 lines>...

    reset_contextvars=reset_contextvars,

    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

)

^

File "/opt/render/project/src/.venv/lib/python3.14/site-packages/uvicorn/main.py", line 620, in run

config.load_app()

\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~^^

File "/opt/render/project/src/.venv/lib/python3.14/site-packages/uvicorn/config.py", line 434, in load_app

return import_from_string(self.app)

File "/opt/render/project/src/.venv/lib/python3.14/site-packages/uvicorn/importer.py", line 19, in import_from_string

module = importlib.import_module(module_str)

File "/opt/render/project/python/Python-3.14.3/lib/python3.14/importlib/__init__.py", line 88, in import_module

return \_bootstrap.\_gcd_import(name[level:], package, level)

       \~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

File "<frozen importlib._bootstrap>", line 1398, in _gcd_import

File "<frozen importlib._bootstrap>", line 1371, in _find_and_load

File "<frozen importlib._bootstrap>", line 1342, in _find_and_load_unlocked

File "<frozen importlib._bootstrap>", line 938, in _load_unlocked

File "<frozen importlib._bootstrap_external>", line 759, in exec_module

File "<frozen importlib._bootstrap>", line 491, in _call_with_frames_removed

File "/opt/render/project/src/app.py", line 16, in <module>

@tool

 ^^^^

File "/opt/render/project/src/.venv/lib/python3.14/site-packages/langchain_core/tools/convert.py", line 375, in tool

return \_create_tool_factory(name_or_callable.\_\_name\_\_)(name_or_callable)

       \~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~^^^^^^^^^^^^^^^^^^

File "/opt/render/project/src/.venv/lib/python3.14/site-packages/langchain_core/tools/convert.py", line 317, in _tool_factory

return StructuredTool.from_function(

       \~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~^

    func,

    ^^^^^

...<9 lines>...

    extras=extras,

    ^^^^^^^^^^^^^^

)

^

File "/opt/render/project/src/.venv/lib/python3.14/site-packages/langchain_core/tools/structured.py", line 290, in from_function

raise ValueError(msg)

ValueError: Function must have a docstring if description not provided.

==> Exited with status 1

==> Common ways to troubleshoot your deploy: https://render.com/docs/troubleshooting-deploys

==> Running 'uvicorn app:app --host 0.0.0.0 --port $PORT'
