"use client"
import React, {useEffect, useState} from "react";
import {Box, Button, CircularProgress, Container, FormControl, InputLabel, MenuItem, Select} from "@mui/material";

function query4() {

    const [number, setNumber] = useState('');
    const [filename, setFilename] = useState('');
    const [procData, setProcData] = useState(null);
    const [loading, setLoading] = useState(false);

    const fetchData = async () => {
    // Use the selectedCountry and filename to construct the API URL
    const apiUrl = `http://localhost:20004/apptest/query4/${number}/${filename}/`;

    try {
        setLoading(true);
        // Fetch data from the API
        const response = await fetch(apiUrl);
        const data = await response.json();
        console.log(data);
        setProcData(data); // Update state with the fetched data
        console.log(procData);
        } catch (error) {
        console.error('Error fetching data:', error);
        } finally {
        setLoading(false);
        }
    };


    useEffect(() => {
        setProcData(null);

    }, [])

    return (
        <>
            <Container maxWidth="100%"
                       sx={{
                           backgroundColor: "white",
                           padding: "2rem",
                           borderRadius: "1rem",
                           border: "solid thin black"
                       }}>
                <Box>
                    <h2 style={{fontSize: "1.5rem", marginBottom: "1rem"}}>Options</h2>
                    <FormControl fullWidth style={{marginTop: '1rem'}}>
                        <InputLabel id="Number-input-label">Number</InputLabel>
                        <input
                            type="number"
                            id="number"
                            value={number}
                            onChange={(e) => setNumber(e.target.value)}
                        />
                    </FormControl>
                    <FormControl fullWidth style={{marginTop: '1rem'}}>
                        <InputLabel id="filename-input-label">Filename</InputLabel>
                        <input
                            type="text"
                            id="filename"
                            value={filename}
                            onChange={(e) => setFilename(e.target.value)}
                        />
                    </FormControl>
                    <Button
                        variant="contained"
                        color="primary"
                        style={{marginTop: '1rem'}}
                        onClick={fetchData}
                        disabled={!number || !filename || loading}
                    >
                        Fetch Data
                    </Button>
                </Box>
            </Container>

            <Container maxWidth="100%" sx={{
                backgroundColor: 'info.dark',
                padding: "2rem",
                marginTop: "2rem",
                borderRadius: "1rem",
                color: "white"
            }}>
                <h1 style={{fontSize: '1.5rem', fontWeight: 'bold'}}>
                    Results <small>(PROC)</small>
                </h1>
                {loading ? (
                    <CircularProgress/>

                ) : procData ? (

                    <ul>
                        {procData.map((data, index) => (
                            <li key={index}>{data.value}</li>
                        ))}
                    </ul>
                ) : (
                    '--'
                )}
            </Container>
        </>
    );
}

export default query4;